#!/usr/bin/env python
 
import csv
import sys
import pprint
 
# Function to convert a csv file to a list of dictionaries.  Takes in one variable called "variables_file"
 
def csv_dict_list(variables_file):
     
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
 
    reader = csv.DictReader(open(variables_file, 'rb'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list
 
# Calls the csv_dict_list function, passing the named csv
 
device_values = csv_dict_list(sys.argv[1])
 
# Prints the results nice and pretty like
 
pprint.pprint(device_values)



'''
               'Matrix Oil Wonders Volume Rose Shampoo Conditioner Liter Duo '
               '33 oz/each'),
              ('primary_asset_url',
               'https://i5.walmartimages.com/asr/e2635da1-5451-462b-994c-55d1d99d5f30_1.a72b98618d75ae3c00c4d005c9df44c0.jpeg'),
              ('offer_lifecycle_status', 'ACTIVE'),
              ('display_status', 'STAGING'),
              ('product_short_description',
               'This is a new liter set of matrix oil wonders volume rose '
               'shampoo conditioner 33. 8 oz each volume rose shampoo '
               'lightweight shampoo is a silicone-free shampoo for fine hair '
               'that is infused with rose hip seed oil. It primes hair by '
               'removing build up and delicately cleansing each strand. Helps '
               'provide softness and shine.'),
              ('product_long_description',
               'This is a new liter set of matrix oil wonders volume rose '
               'shampoo conditioner 33. 8 oz each volume rose shampoo '
               'lightweight shampoo is a silicone-free shampoo for fine hair '
               'that is infused with rose hip seed oil. It primes hair by '
               'removing build up and delicately cleansing each strand. Helps '
               'provide softness and shine.<br/><ul><li>Volume rose '
               'conditionerthis conditioner is infused with rose hip seed oil '
               'and is silicone free as well. It helps provide nourishment to '
               'delicate strands.</li></ul>'),
              ('primary_shelf (id)', '1007000'),
              ('primary_shelf', 'Conditioners'),
              ('all_shelves (id)', '1007000, 1007001'),
              ('all_shelves', 'Conditioners, Shampoos'),
              ('pch_id', ''),
              ('category', ''),
              ('product_type', 'Shampoo & Conditioner Sets'),
              ('abstract_product_id', ''),
              ('product_class_type', 'REGULAR'),
              ('brand', 'Matrix'),
              ('size', '8.45 oz'),
              ('volume_capacity', ''),
              ('target_audience', ''),
              ('gender', 'Unisex'),
              ('dispenser_included', ''),
              ('ib_ingredient_preference', ''),
              ('ingredients', ''),
              ('has_ingredient_list', ''),
              ('ib_hair_care_key_benefits', ''),
              ('hair_type', ''),
              ('age_group', ''),
              ('ib_scent_family', ''),
              ('scent', ''),
              ('DM', '')]),
 OrderedDict([('check', 'http://www.walmart.com/ip/10323632'),
              ('image_size_100', ''),
              ('quick_links', ''),
              ('product_id', '7H65985QQEA1'),
              ('item_id', '10323632'),
              ('product_name',
               'Motions Shampoo, Lavish Conditioning, Medium to Coarse Hair, '
               '13 oz.'),
              ('primary_asset_url',
               'https://i5.walmartimages.com/asr/0855f7bd-bfeb-4fab-9cca-4a43dbd94f58_1.7e176aadcfd6f44a2d227aa94acf0094.jpeg'),
              ('offer_lifecycle_status', 'ACTIVE'),
              ('display_status', 'STAGING'),
              ('product_short_description',
               '<p>Designed for all hair textures women with relaxed, natural '
               'and textured hair, Motions Lavish Conditioning Shampoo helps '
               'keep hair soft and silky. Ideal for weekly hair washing, this '
               'moisture-rich conditioning shampoo cleans, conditions, and '
               'detangles. Directions: Rinse relaxer thoroughly from '
               'hair.&nbsp; Apply Moisture Plus Conditioner for ten minutes '
               'and rinse.&nbsp; Shampoo with Motions Neutralizing Shampoo and '
               'rinse.&nbsp; Then apply Lavish Conditioning Shampoo, lather '
               'and rinse.</p>'),
              ('product_long_description',
               '<p><strong>Motions Lavish Conditioning Shampoo, 13 '
               'oz</strong></p><ul>\t<li>Motions Lavish Conditioning Shampoo, '
               'Medium to Coarse HairRevitalizes hair, formulated with a blend '
               'of gentle cleansers and nourishing emollients.</li>\t'
               '<li>Protects hair while helping to restore its natural '
               'moisture balance.</li>\t<li>Silk and keratin proteins help to '
               'keep hair healthy and strong with an ultra-glossy '
               'sheen.Designed for all hair textures women with relaxed, '
               'natural and textured hair.</li>\t<li>Helps to keep hair soft '
               'and silky.</li>\t<li>Ideal for weekly hair washing, this '
               'moisture-rich conditioning shampoo cleans, conditions, and '
               'detangles.</li></ul>'),
              ('primary_shelf (id)', '1007001, -1'),
              ('primary_shelf', 'Shampoos, UNNAV'),
              ('all_shelves (id)', '1007001, -1'),
              ('all_shelves', 'Shampoos, UNNAV'),
              ('pch_id', '4008299'),
              ('category', 'Shampoos'),
              ('product_type', 'Conditioning Shampoos'),
              ('abstract_product_id', ''),
              ('product_class_type', 'REGULAR'),
              ('brand', 'Motions'),
              ('size', '13 oz'),
              ('volume_capacity', ''),
              ('target_audience', ''),
              ('gender', 'Unisex'),
              ('dispenser_included', ''),
              ('ib_ingredient_preference', ''),
              ('ingredients',
               'Aqua, Sodium Lauryl Sulfate, Cocamidopropyl Betaine, '
               'PPG-5-Ceteth-10 Phosphate, Disodium Cocoamphodipropionate, '
               'PEG-30 Glyceryl Cocoate, Hydrolyzed Keratin, Hydrolyzed Silk '
               '(Serica), Cocotrimonium Chloride, Glycol Distearate, Sdoium '
               'C14-17 Alkyl Sec Sulfonate, Propylene Glycol, PEG-120 Methyl '
               'Glucose Dioleate, PEG-12 Diemthicone, Polyquaternium-10, '
               'Citric Acid, Methylparaben, Propylparaben, Diaxolidinyl Urea, '
               'Linalool, Parfum/Fragrance.'),
              ('has_ingredient_list', 'No'),
              ('ib_hair_care_key_benefits', ''),
              ('hair_type', 'Coarse, Normal'),
              ('age_group', ''),
              ('ib_scent_family', ''),
              ('scent', ''),
              ('DM', '')]),
 OrderedDict([('check', 'http://www.walmart.com/ip/103689897'),
              ('image_size_100', ''),
              ('quick_links', ''),
              ('product_id', '38P85RTYDEF9'),
              ('item_id', '103689897'),
              ('product_name',
               'Matrix  Biolage Advanced Fiberstrong Bamboo 13.5-ounce Shampoo '
               'and Conditioner'),
              ('primary_asset_url',
               'https://i5.walmartimages.com/asr/d1da1587-d077-453f-a242-c2dcf6e0c8f8_1.e2c5456147edfae09e20fed25e1a45fc.jpeg'),
              ('offer_lifecycle_status', 'ACTIVE'),
              ('display_status', 'STAGING'),
              ('product_short_description',
               'Matrix Biolage Advanced Fiberstrong Bamboo 13.5-ounce Shampoo '
               'and Conditioner<p>Biolage Advanced Fiberstrong helps '
               'strengthen weak hair, formulated with the power of '
               'Intra-Cylane plus Bamboo and Ceramide to help fill in the hair '
               'structure. This formula helps fortify fragile areas as it '
               'conditions for super-charged strength with a soft '
               'touch.<br><br><ul><li>Size: Shampoo: 13.9 ounces; Conditioner: '
               '8'),
              ('product_long_description',
               'Biolage Advanced Fiberstrong helps strengthen weak hair, '
               'formulated with the power of Intra-Cylane plus Bamboo and '
               'Ceramide to help fill in the hair structure. This formula '
               'helps fortify fragile areas as it conditions for super-charged '
               'strength with a soft touch.<br><br><ul><li>Size: Shampoo: 13.9 '
               'ounces; Conditioner: 8.5 ounces</li><li>Quantity: One (1) '
               'shampoo and one (1) conditioner</li><li>Targeted area: '
               'Hair</li><li>Hair type: Weak, chemically-treated '
               'hair</li><li>Active ingredients: </li></ul></uL>'),
              ('primary_shelf (id)', '1007000'),
              ('primary_shelf', 'Conditioners'),
              ('all_shelves (id)', '1007000, 1007001'),
              ('all_shelves', 'Conditioners, Shampoos'),
              ('pch_id', ''),
              ('category', ''),
              ('product_type', 'Shampoo & Conditioner Sets'),
              ('abstract_product_id', ''),
              ('product_class_type', 'REGULAR'),
              ('brand', 'Matrix'),
              ('size', ''),
              ('volume_capacity', ''),
              ('target_audience', ''),
              ('gender', 'Unisex'),
              ('dispenser_included', ''),
              ('ib_ingredient_preference', ''),
              ('ingredients', ''),
              ('has_ingredient_list', ''),
              ('ib_hair_care_key_benefits', ''),
              ('hair_type', ''),
              ('age_group', ''),
              ('ib_scent_family', ''),
              ('scent', ''),
              ('DM', '')]),
 OrderedDict([('check', 'http://www.walmart.com/ip/105024531'),
              ('image_size_100', ''),
              ('quick_links', ''),
              ('product_id', '1XDP73TXR6S3'),
              ('item_id', '105024531'),
              ('product_name', 'Attitude Shampoo Color Protection - 12 Oz'),
              ('primary_asset_url',
               'https://i5.walmartimages.com/asr/37a6150e-9145-4dfb-990b-722ac06cdb5a_1.7d97b4dca1b4853aa932a6b1cd8d14aa.jpeg'),
              ('offer_lifecycle_status', 'ACTIVE'),
              ('display_status', 'STAGING'),
              ('product_short_description',
               'Cleanses hair without damaging and healthy, shiny.'),
              ('product_long_description',
               'UPC: 626232110036 - Attitude Shampoo Color Protection - 12 Oz '
               '- Cleanses hair without damaging and healthy, shiny. - <span '
               'class="manu">MANUFACTURER: </span><span '
               'class="greenletters">Attitude </span></br><strong>Attitude '
               'Shampoo Color Protection</strong><ul><li>Carcinogen free '
               'ingredients or by-products (IARC group 1 &amp; 2)</li><li>Free '
               'of 1,4-dioxane and ethylene oxide, tested by independent '
               'laboratory</li><li>Certified eco-friendly by EcoLogo, the most '
               'recognized certification in North America</li><li>CO2 NEUTRAL: '
               'no contribution to climate change</li><li>Vegetable-based and '
               'biodegradable (OECD 301)</li><li>Fragrance derived from '
               'natural ingredients, hypoallergenic, respect IFRA '
               '(International Fragrance Association) '
               'standards</li><li>Fragrance without CMR (Carcinogens, Mutagens '
               'or toxic for Reproduction) compounds</li><li>Not tested on '
               'animal</li><li>Vegan product</li><li>Septic tank '
               'safe</li></ul>'),
              ('primary_shelf (id)', '1007001'),
              ('primary_shelf', 'Shampoos'),
              ('all_shelves (id)', '1007001'),
              ('all_shelves', 'Shampoos'),
              ('pch_id', ''),
              ('category', ''),
              ('product_type', 'Shampoos'),
              ('abstract_product_id', ''),
              ('product_class_type', 'REGULAR'),
              ('brand', 'Attitude WellBeing'),
              ('size', '1'),
              ('volume_capacity', ''),
              ('target_audience', ''),
              ('gender', 'Unisex'),
              ('dispenser_included', ''),
              ('ib_ingredient_preference', ''),
              ('ingredients', ''),
              ('has_ingredient_list', ''),
              ('ib_hair_care_key_benefits', ''),
              ('hair_type', ''),
              ('age_group', ''),
              ('ib_scent_family', ''),
              ('scent', ''),
              ('DM', '')]),
 OrderedDict([('check', 'http://www.walmart.com/ip/105092897'),
              ('image_size_100', ''),
              ('quick_links', ''),
              ('product_id', '7GIQ8VH8A34W'),
              ('item_id', '105092897'),
              ('product_name',
               'Tressa Water Colors Crimson Splash Shampoo 8.5 oz'),
              ('primary_asset_url',
               'https://i5.walmartimages.com/asr/de4fd48f-3985-41f6-acde-1d5bb9a58776_1.579006be8dd9e9d20a774227292262cd.jpeg'),
              ('offer_lifecycle_status', 'ACTIVE'),
              ('display_status', 'STAGING'),
              ('product_short_description',
               'Watercolors is a gentle, color infusing shampoo that enriches '
               'the vibrancy and health of color-treated hair between salon '
               'visits. Apply to wet hair. Lather 2-3 minutes. Rinse. Repeat '
               'for added intensity.'),
              ('product_long_description',
               'Watercolors is a gentle, color infusing shampoo that enriches '
               'the vibrancy and health of color-treated hair between salon '
               'visits. Apply to wet hair. Lather 2-3 minutes. Rinse. Repeat '
               'for added intensity.'),
              ('primary_shelf (id)', '1007001'),
              ('primary_shelf', 'Shampoos'),
              ('all_shelves (id)', '1007001'),
              ('all_shelves', 'Shampoos'),
              ('pch_id', ''),
              ('category', ''),
              ('product_type', 'Shampoos'),
              ('abstract_product_id', ''),
              ('product_class_type', 'REGULAR'),
              ('brand', 'Tressa'),
              ('size', '8.1 - 9 Oz.'),
              ('volume_capacity', ''),
              ('target_audience', ''),
              ('gender', 'Unisex'),
              ('dispenser_included', ''),
              ('ib_ingredient_preference', ''),
              ('ingredients', ''),
              ('has_ingredient_list', ''),
              ('ib_hair_care_key_benefits', ''),
              ('hair_type', ''),
              ('age_group', ''),
              ('ib_scent_family', ''),
              ('scent', ''),
              ('DM', '')]),
 OrderedDict([('check', 'http://www.walmart.com/ip/105115125'),
              ('image_size_100', ''),
              ('quick_links', ''),
              ('product_id', '5LJG5S6HYPQE'),
              ('item_id', '105115125'),
              ('product_name', 'Pf Tropics Shampoo Gal Pina Colda'),
              ('primary_asset_url',
               'https://i5.walmartimages.com/asr/23b8a613-0a08-4beb-843e-c2e80e056004_1.dba676c77079feec942522e2fa2d3686.jpeg'),
              ('offer_lifecycle_status', 'ACTIVE'),
              ('display_status', 'STAGING'),
              ('product_short_description',
               'Pf Tropics Shampoo Gal Pina Colda'),
              ('product_long_description',
               'Gentle enough to be used everyday, these enticing Pet Effects '
               'Tropics Collection Shampoos conjure up the scents of a '
               'tropical getaway and leave coats clean, soft, and silky to '
               'touch.'),
              ('primary_shelf (id)', '1007001'),
              ('primary_shelf', 'Shampoos'),
              ('all_shelves (id)', '1007001'),
              ('all_shelves', 'Shampoos'),
              ('pch_id', ''),
              ('category', ''),
              ('product_type', 'Animal Shampoos & Conditioners'),
              ('abstract_product_id', ''),
              ('product_class_type', 'REGULAR'),
              ('brand', 'PetEdge'),
              ('size', ''),
              ('volume_capacity', ''),
              ('target_audience', ''),
              ('gender', ''),
              ('dispenser_included', ''),
              ('ib_ingredient_preference', ''),
              ('ingredients', ''),
              ('has_ingredient_list', ''),
              ('ib_hair_care_key_benefits', ''),
              ('hair_type', ''),
              ('age_group', ''),
              ('ib_scent_family', ''),
              ('scent', ''),
              ('DM', '')]),
 OrderedDict([('check', 'http://www.walmart.com/ip/105304179'),
              ('image_size_100', ''),
              ('quick_links', ''),
              ('product_id', '3LJYB5136NHC'),
              ('item_id', '105304179'),
              ('product_name',
               'Bain De Terre - Green Meadow Balancing Shampoo (For Normal to '
               'Oily Hair) - 400ml/13.5oz'),
              ('primary_asset_url',
               'https://i5.walmartimages.com/asr/b4472c78-e28d-47d1-a95f-d192528bcf8c_1.30e8603085bff5c226afa4803f5c2803.jpeg'),
              ('offer_lifecycle_status', 'ACTIVE'),
              ('display_status', 'STAGING'),
              ('product_short_description',
               'A color-safe, paraben-free balancing shampooFormulated with '
               'green meadows extracts, precious argan & monoi oilsHelps '
               'cleanse hair while restoring optimal hydration balanceLeaves '
               'hair soft, smooth, lustrous & healthy lookingIdeal for normal '
               'to oily hair'),
              ('product_long_description',
               'A color-safe, paraben-free balancing shampooFormulated with '
               'green meadows extracts, precious argan & monoi oilsHelps '
               'cleanse hair while restoring optimal hydration balanceLeaves '
               'hair soft, smooth, lustrous & healthy lookingIdeal for normal '
               'to oily hair'),
              ('primary_shelf (id)', '1007001'),
              ('primary_shelf', 'Shampoos'),
              ('all_shelves (id)', '1007001'),
              ('all_shelves', 'Shampoos'),
              ('pch_id', ''),
              ('category', ''),
              ('product_type', 'Shampoos'),
              ('abstract_product_id', ''),
              ('product_class_type', 'REGULAR'),
              ('brand', 'Bain De Terre - Hair Care'),
              ('size', ''),
              ('volume_capacity', ''),
              ('target_audience', ''),
              ('gender', ''),
              ('dispenser_included', ''),
              ('ib_ingredient_preference', ''),
              ('ingredients', ''),
              ('has_ingredient_list', ''),
              ('ib_hair_care_key_benefits', ''),
              ('hair_type', ''),
              ('age_group', ''),
              ('ib_scent_family', ''),
              ('scent', ''),
              ('DM', '')]),
 OrderedDict([('check', 'http://www.walmart.com/ip/105563337'),
              ('image_size_100', ''),
              ('quick_links', ''),
              ('product_id', '2M9D8ISPCRRB'),
              ('item_id', '105563337'),
              ('product_name',
               'Color Wow Root Cover Up Blonde Hair (Blonde) 2.1 g 0.07 oz'),
              ('primary_asset_url',
               'http://i5.walmartimages.com/asr/58efc92b-eb3e-4312-9805-93c9db3543bf_1.c3842084fa882325102225c45d850420.jpeg'),
              ('offer_lifecycle_status', 'ACTIVE'),
              ('display_status', 'STAGING'),
              ('product_short_description',
               "Those dreaded roots are No match for the 'WOW' Root Concealer "
               'that will camouflage those unwanted roots while adhering to '
               'hair without being sticky. A water-resistant formula means the '
               'results last from shampoo to shampoo, but you can swim, sweat '
               'and sleep and the powder will stay in place.'),
              ('product_long_description',
               "Those dreaded roots are No match for the 'WOW' Root Concealer "
               'that will camouflage those unwanted roots while adhering to '
               'hair without being sticky. A water-resistant formula means the '
               'results last from shampoo to shampoo, but you can swim, sweat '
               'and sleep and the powder will stay in place.'),
              ('primary_shelf (id)', '1007001'),
              ('primary_shelf', 'Shampoos'),
              ('all_shelves (id)', '1007001'),
              ('all_shelves', 'Shampoos'),
              ('pch_id', ''),
              ('category', ''),
              ('product_type', 'Shampoos'),
              ('abstract_product_id', ''),
              ('product_class_type', 'REGULAR'),
              ('brand', 'Color Wow'),
              ('size', ''),
              ('volume_capacity', ''),
              ('target_audience', ''),
              ('gender', ''),
              ('dispenser_included', ''),
              ('ib_ingredient_preference', ''),
              ('ingredients', ''),
              ('has_ingredient_list', ''),
              ('ib_hair_care_key_benefits', ''),
              ('hair_type', ''),
              ('age_group', ''),
              ('ib_scent_family', ''),
              ('scent', ''),
              ('DM', '')]),
 OrderedDict([('check', 'http://www.walmart.com/ip/106035915'),
              ('image_size_100', ''),
              ('quick_links', ''),
              ('product_id', '2IS12XBMXGKX'),
              ('item_id', '106035915'),
              ('product_name',
               'Revlon ColorSilk Bold Black 1 ColorStay Moisturizing Shampoo, '
               '8.45 fl oz'),
              ('primary_asset_url',
               'https://i5.walmartimages.com/asr/27bc08d9-b9fd-487d-8a93-79af3e454c74_1.4a95b8cdb620a7d777589db51d01200e.jpeg'),
              ('offer_lifecycle_status', 'ACTIVE'),
              ('display_status', 'STAGING'),
              ('product_short_description',
               'Bold Black� 1 Colorstay Moisturizing '
               'Shampoo�<br/><br/>Formulated with rich black tones and acai '
               'berry, ColorSilk Bold Black� Shampoo protects color, provides '
               'shine and moisturizes hair.'),
              ('product_long_description',
               '<div><b>Product Features</b><ul><li>Protects '
               'color</li><li>Provides shine</li><li>Shampooing '
               'hydratant</li></ul></div><br/><br/>Revlon Cons., Prod., '
               'Corp.,<br/>N.Y., NY, '
               '10004.<br/><br/>www.colorsilk.com<br/><br/>�2016'),
              ('primary_shelf (id)', '1007001, -1'),
              ('primary_shelf', 'Shampoos, UNNAV'),
              ('all_shelves (id)', '1007001, -1'),
              ('all_shelves', 'Shampoos, UNNAV'),
              ('pch_id', '4008297'),
              ('category', 'Shampoos'),
              ('product_type', 'Shampoos'),
              ('abstract_product_id', '57Z7CRPOOXBL'),
              ('product_class_type', 'VARIANT'),
              ('brand', 'Revlon'),
              ('size', ''),
              ('volume_capacity', ''),
              ('target_audience', ''),
              ('gender', ''),
              ('dispenser_included', ''),
              ('ib_ingredient_preference', ''),
              ('ingredients', ''),
              ('has_ingredient_list', ''),
              ('ib_hair_care_key_benefits', ''),
              ('hair_type', ''),
              ('age_group', ''),
              ('ib_scent_family', ''),
              ('scent', ''),
              ('DM', '')]),
 OrderedDict([('check', 'http://www.walmart.com/ip/106035915'),
              ('image_size_100', ''),
              ('quick_links', ''),
              ('product_id', '57Z7CRPOOXBL'),
              ('item_id', '106035915'),
              ('product_name',
               'Revlon ColorSilk Bold Black 1 ColorStay Moisturizing Shampoo, '
               '8.45 fl oz'),
              ('primary_asset_url',
               'https://i5.walmartimages.com/asr/27bc08d9-b9fd-487d-8a93-79af3e454c74_1.4a95b8cdb620a7d777589db51d01200e.jpeg'),
              ('offer_lifecycle_status', 'ACTIVE'),
              ('display_status', 'STAGING'),
              ('product_short_description',
               'Bold Black� 1 Colorstay Moisturizing '
               'Shampoo�<br/><br/>Formulated with rich black tones and acai '
               'berry, ColorSilk Bold Black� Shampoo protects color, provides '
               'shine and moisturizes hair.'),
              ('product_long_description',
               '<div><b>Product Features</b><ul><li>Protects '
               'color</li><li>Provides shine</li><li>Shampooing '
               'hydratant</li></ul></div><br/><br/>Revlon Cons., Prod., '
               'Corp.,<br/>N.Y., NY, '
               '10004.<br/><br/>www.colorsilk.com<br/><br/>�2016'),
              ('primary_shelf (id)', '1007001, -1'),
              ('primary_shelf', 'Shampoos, UNNAV'),
              ('all_shelves (id)', '1007001, -1'),
              ('all_shelves', 'Shampoos, UNNAV'),
              ('pch_id', '4008297'),
              ('category', 'Shampoos'),
              ('product_type', 'Shampoos'),
              ('abstract_product_id', ''),
              ('product_class_type', 'BVSHELL'),
              ('brand', 'Revlon'),
              ('size', ''),
              ('volume_capacity', ''),
              ('target_audience', ''),
              ('gender', ''),
              ('dispenser_included', ''),
              ('ib_ingredient_preference', ''),
              ('ingredients', ''),
              ('has_ingredient_list', ''),
              ('ib_hair_care_key_benefits', ''),
              ('hair_type', ''),
              ('age_group', ''),
              ('ib_scent_family', ''),
              ('scent', ''),
              ('DM', '')])]
'''
