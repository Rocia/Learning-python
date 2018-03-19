import lupa
from lupa import LuaRuntime
lua = LuaRuntime(unpack_returned_tuples=True)

def call_lua_with_args(script, args):
    lua.eval(script,*args)

lua_script = """
local campID  = '994'
local cookieID   = '322efe3d-a0ff-4764-b01e-1b0459888a56'
local CPM = '0.1'

local segList, check_keys, return_list, cookieFromSegments, costofqualified,pricing_LOT, pricing_VTZ, pricing_LRP, costperDMP={}, {}, {}, {}, {}, {}, {}, {}, {}
local hashkey,KEYS_SIZE,qualified, log
local DMPS = {'LOT','VTZ','LRP'}
local entries     = '40000000'
local precision   = '0.01' 
local hash = redis.sha1hex(cookieID)
local h = { }
h[0] = tonumber(string.sub(hash, 1 , 8 ), 16)
h[1] = tonumber(string.sub(hash, 9 , 16), 16)
h[2] = tonumber(string.sub(hash, 17, 24), 16)
h[3] = tonumber(string.sub(hash, 25, 32), 16)


redis.call('select',2) 
segList = redis.call('SMEMBERS','camp_targeting:' .. campID) 
KEYS_SIZE = 0   
for i,v in ipairs(segList) do KEYS_SIZE = KEYS_SIZE+1 end
 
 
redis.call('select',3) 
for xy=1,KEYS_SIZE,1
do
  local count     = redis.call('GET', 'audience_targeting:' .. segList[xy] .. ':count')
  if count then
    local b = { }
    local factor = math.ceil((entries + count) / entries)
    local index = math.ceil(math.log(factor) / 0.69314718055995)
    local scale = math.pow(2, index - 1) * entries
    local maxbits = math.floor((scale * math.log(precision * math.pow(0.5, index))) / -0.4804530139182)
    local maxk = math.floor(0.69314718055995 * maxbits / scale)
    for i=1, maxk do
      table.insert(b, h[i % 2] + i * h[2 + (((i + (i % 2)) % 4) / 2)])
    end
    for n=1, index do  
      local key    = 'audience_targeting:' .. segList[xy] .. ':' .. n
      local found  = true
      local scalen = math.pow(2, n - 1) * entries
      local bits = math.floor((scalen * math.log(precision * math.pow(0.5, n))) / -0.4804530139182)
      local k = math.floor(0.69314718055995 * bits / scalen)
      for i=1, k do
        if redis.call('GETBIT', key, b[i] % bits) == 0 then
          found = false
          break
        end
      end
      if found then
        table.insert(return_list,1)
        table.insert(cookieFromSegments,segList[xy])
      else
        table.insert(return_list,0)
      end
    end
  else
    table.insert(return_list,0)
  end
end 

qualified = 0
for i,v in ipairs(cookieFromSegments) do qualified = qualified+1 end
redis.call('select',2)
for xy=1,qualified,1 do
  local cost = redis.call('GET', 'segment_wise_cost:' .. cookieFromSegments[xy] .. ':cost')
  costofqualified[cookieFromSegments[xy]] = cost
end

function string.starts(String,Start)
   return string.sub(String,1,string.len(Start))==Start
end

local highest_LOT, highest_LRP, highest_VTZ = 0,0,0
for i,v in pairs(costofqualified) do 
  if string.starts(i,'LOT') then
    table.insert(pricing_LOT, '['..i..'|'..v..'|'..v..']')
    local vnum = tonumber(v)
    if vnum > highest_LOT then highest_LOT = vnum costperDMP['LOT']= v end
  end
  if string.starts(i,'VTZ') then
    table.insert(pricing_VTZ, '['..i..'|'..v..'|'..v..']')
    local vnum = tonumber(v)
    if vnum > highest_VTZ then highest_VTZ = vnum costperDMP['VTZ']= v end
  end
  if string.starts(i,'LRP') then
    table.insert(pricing_LRP, '['..i..'|'..v..'|'..v..']')
    local vnum = tonumber(v)
    if vnum > highest_LRP then highest_LRP = vnum costperDMP['LRP']=v end
  end  
end

for xy = 1, 3, 1 do
  if xy == 1 and next(pricing_LOT) then
    for yz= 1,qualified,1 do
        local record = pricing_LOT[xy]
        local cost_of_seg = string.match(record, '|(%d.%d)|')
        if tonumber(cost_of_seg) ~= highest_LOT then pricing_LOT[xy] = string.gsub(record, '|%d.%d]', '|0]') end
    if tonumber(cost_of_seg) == highest_LOT then pricing_LOT[xy] = string.gsub(record, '|%d.%d]', '|0]') break end
    local log = log .. string.gsub(record, '|%d.%d]', '|0];')
    end
  end
  if xy == 2 and next(pricing_VTZ) then
    for yz= 1,qualified,1 do
        local record = pricing_VTZ[xy]
        local cost_of_seg = string.match(record, '|(%d.%d)|')
        if tonumber(cost_of_seg) ~= highest_VTZ then pricing_VTZ[xy] = string.gsub(record, '|%d.%d]', '|0]') end
    if tonumber(cost_of_seg) == highest_VTZ then pricing_VTZ[xy] = string.gsub(record, '|%d.%d]', '|0]') break end
    local log = log .. string.gsub(record, '|%d.%d]', '|0];')  
    end
  end
  if xy == 3 and next(pricing_LRP) then
    for yz= 1,qualified,1 do
        local record = pricing_LRP[xy]
        local cost_of_seg = string.match(record, '|(%d.%d)|')
        if tonumber(cost_of_seg) ~= highest_LRP then pricing_LRP[xy] = string.gsub(record, '|%d.%d]', '|0]') end
    if tonumber(cost_of_seg) == highest_LRP then pricing_LRP[xy] = string.gsub(record, '|%d.%d]', '|0]') break end
    local log = log .. string.gsub(record, '|%d.%d]', '|0];')  
    end
  end
end

local totalCPM = (CPM+highest_LOT+highest_LRP+highest_VTZ)/1000

redis.call('select','0')
local budget = redis.call('get','campaignsRequest:campaign_'..campID)
local Balance = tonumber(string.format('%.6f', budget-totalCPM))
local success = redis.call('set','campaignsRequest:campaign_'..campID, Balance)
for i,v in pairs(success) do 
  if v == 'OK' then
    return 1
  else 
    return -1
  end
end
"""
if __name__ == "__main__":
    call_lua_with_args(lua_script,[994, '322efe3d-a0ff-4764-b01e-1b0459888a56', 0.1])

