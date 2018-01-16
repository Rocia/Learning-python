from crontab import CronTab

empty_cron = CronTab()
my_user_cron = CronTab(user=True)
users_cron = CronTab(user='username')

And two ways from non-system sources that will work on Windows too::

file_cron = CronTab(tabfile='filename.tab')
mem_cron = CronTab(tab="""
* * * * * command
""")

Special per-command user flag for vixie cron format (new in 1.9)::

system_cron = CronTab(tabfile='/etc/crontab', user=False)
job = system_cron[0]
job.user != None
system_cron.new(command='new_command', user='root')

Creating a new job is as simple as::

job = cron.new(command='/usr/bin/echo')

And setting the job's time restrictions::

job.minute.during(5,50).every(5)
job.hour.every(4)
job.day.on(4, 5, 6)

job.dow.on('SUN')
job.dow.on('SUN', 'FRI')
job.month.during('APR', 'NOV')

Each time restriction will clear the previous restriction::

job.hour.every(10) # Set to * */10 * * *
job.hour.on(2) # Set to * 2 * * *

Appending restrictions is explicit::

job.hour.every(10) # Set to * */10 * * *
job.hour.also.on(2) # Set to * 2,*/10 * * *

Setting all time slices at once::

job.setall(2, 10, '2-4', '*/2', None)
job.setall('2 10 * * *')

Setting the slice to a python date object::

job.setall(time(10, 2))
job.setall(date(2000, 4, 2))
job.setall(datetime(2000, 4, 2, 10, 2))

Run a jobs command. Running the job here will not effect it's
existing schedule with another crontab process::

job_standard_output = job.run()

Creating a job with a comment::

job = cron.new(command='/foo/bar', comment='SomeID')

Get the comment or command for a job::

command = job.command
comment = job.comment

Modify the comment or command on a job::

job.set_command("new_script.sh")
job.set_comment("New ID or comment here")

Disabled or Enable Job::

job.enable()
job.enable(False)
False == job.is_enabled()

Validity Check::

True == job.is_valid()

Use a special syntax::

job.every_reboot()

Find an existing job by command sub-match or regular expression::

iter = cron.find_command('bar') # matches foobar1
iter = cron.find_command(re.compile(r'b[ab]r$'))

Find an existing job by comment exact match or regular expression::

iter = cron.find_comment('ID or some text')
iter = cron.find_comment(re.compile(' or \w'))

Find an existing job by schedule::

iter = cron.find_time(2, 10, '2-4', '*/2', None)
iter = cron.find_time("*/2 * * * *")

Clean a job of all rules::

job.clear()

Iterate through all jobs, this includes disabled (commented out) cron jobs::

for job in cron:
print job

Iterate through all lines, this includes all comments and empty lines::

for line in cron.lines:
print line

Remove Items::

cron.remove( job )
cron.remove_all('echo')
cron.remove_all(comment='foo')
cron.remove_all(time='*/2')

Clear entire cron of all jobs::

cron.remove_all()

Write CronTab back to system or filename::

cron.write()

Write CronTab to new filename::

cron.write( 'output.tab' )

Write to this user's crontab (unix only)::

cron.write_to_user( user=True )

Write to some other user's crontab::

cron.write_to_user( user='bob' )

Validate a cron time string::

from crontab import CronSlices
bool = CronSlices.is_valid('0/2 * * * *')


