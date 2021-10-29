import requests


class TestPosts:
    endpoint_products = 'http://127.0.0.1:8000/api/v1/products/'

    def test_get_products(self):
        products = requests.get(url=self.endpoint_products)
        assert products.status_code == 200

    def test_get_product(self):
        product = requests.get(url=f'{self.endpoint_products}2/')
        assert product.status_code == 200

    def test_post_product(self):
        new_product = {
            "code": "00001",
            "status": "published",
            "url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "creator": "speedy",
            "product_name": "product 1",
            "generic_name": "product",
            "quantity": "10",
            "packaging": "product",
            "packaging_tags": "product",
            "brands": "product",
            "brands_tags": "product",
            "categories": "food",
            "categories_tags": "food",
            "origins": "factory",
            "origins_tags": "factory",
            "manufacturing_places": "brazil",
            "manufacturing_places_tags": "brazil",
            "labels": "food",
            "labels_tags": "food",
            "emb_codes": "00001",
            "emb_codes_tags": "000001",
            "cities": "sp",
            "cities_tags": "sp",
            "purchase_places": "brazil",
            "stores": "brazil",
            "countries": "brazil",
            "ingredients_text": "brazil",
            "allergens": "brazil",
            "allergens_tags": "brazil",
            "traces": "brazil",
            "traces_tags": "brazil",
            "serving_size": "product",
            "serving_quantity": "product",
            "no_nutriments": "product",
            "additives_n": "product",
            "additives_tags": "product",
            "ingredients_from_palm_oil_n": "1",
            "ingredients_from_palm_oil": "1",
            "ingredients_from_palm_oil_tags": "2",
            "ingredients_that_may_be_from_palm_oil_n": "2",
            "ingredients_that_may_be_from_palm_oil": "3",
            "ingredients_that_may_be_from_palm_oil_tags": "4",
            "nutriscore_score": "10",
            "nutriscore_grade": "10",
            "nova_group": "food",
            "pnns_groups_1": "food",
            "pnns_groups_2": "food",
            "states": "sp",
            "main_category": "food",
            "image_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_small_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_front_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_front_small_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_ingredients_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_ingredients_small_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_nutrition_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_nutrition_small_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "energy_kj_100g": "10",
            "energy_kcal_100g": "10",
            "energy_100g": "10",
            "energy_from_fat_100g": "10",
            "fat_100g": "10",
            "saturated_fat_100g": "10",
            "butyric_acid_100g": "10",
            "caproic_acid_100g": "10",
            "caprylic_acid_100g": "10",
            "capric_acid_100g": "10",
            "lauric_acid_100g": "10",
            "myristic_acid_100g": "10",
            "palmitic_acid_100g": "10",
            "stearic_acid_100g": "10",
            "arachidic_acid_100g": "10",
            "behenic_acid_100g": "10",
            "lignoceric_acid_100g": "10",
            "cerotic_acid_100g": "10",
            "montanic_acid_100g": "10",
            "melissic_acid_100g": "10",
            "monounsaturated_fat_100g": "10",
            "polyunsaturated_fat_100g": "10",
            "omega_3_fat_100g": "10",
            "alpha_linolenic_acid_100g": "10",
            "eicosapentaenoic_acid_100g": "10",
            "docosahexaenoic_acid_100g": "10",
            "omega_6_fat_100g": "10",
            "linoleic_acid_100g": "10",
            "arachidonic_acid_100g": "10",
            "gamma_linolenic_acid_100g": "10",
            "dihomo_gamma_linolenic_acid_100g": "10",
            "omega_9_fat_100g": "10",
            "oleic_acid_100g": "10",
            "elaidic_acid_100g": "10",
            "gondoic_acid_100g": "10",
            "mead_acid_100g": "10",
            "erucic_acid_100g": "10",
            "nervonic_acid_100g": "10",
            "trans_fat_100g": "10",
            "cholesterol_100g": "10",
            "carbohydrates_100g": "10",
            "sugars_100g": "10",
            "sucrose_100g": "10",
            "glucose_100g": "10",
            "fructose_100g": "10",
            "lactose_100g": "10",
            "maltose_100g": "10",
            "maltodextrins_100g": "10",
            "starch_100g": "10",
            "polyols_100g": "10",
            "fiber_100g": "10",
            "proteins_100g": "10",
            "casein_100g": "10",
            "serum_proteins_100g": "10",
            "nucleotides_100g": "10",
            "salt_100g": "10",
            "sodium_100g": "10",
            "alcohol_100g": "10",
            "vitamin_a_100g": "10",
            "beta_carotene_100g": "10",
            "vitamin_d_100g": "10",
            "vitamin_e_100g": "10",
            "vitamin_k_100g": "10",
            "vitamin_c_100g": "10",
            "vitamin_b1_100g": "10",
            "vitamin_b2_100g": "10",
            "vitamin_pp_100g": "10",
            "vitamin_b6_100g": "10",
            "vitamin_b9_100g": "10",
            "folates_100g": "10",
            "vitamin_b12_100g": "10",
            "biotin_100g": "10",
            "pantothenic_acid_100g": "10",
            "silica_100g": "10",
            "bicarbonate_100g": "10",
            "potassium_100g": "10",
            "chloride_100g": "10",
            "calcium_100g": "10",
            "phosphorus_100g": "10",
            "iron_100g": "10",
            "magnesium_100g": "10",
            "zinc_100g": "10",
            "copper_100g": "10",
            "manganese_100g": "10",
            "fluoride_100g": "10",
            "selenium_100g": "10",
            "chromium_100g": "10",
            "molybdenum_100g": "10",
            "iodine_100g": "10",
            "caffeine_100g": "10",
            "taurine_100g": "10",
            "ph_100g": "10",
            "fruits_vegetables_nuts_100g": "10",
            "fruits_vegetables_nuts_dried_100g": "10",
            "fruits_vegetables_nuts_estimate_100g": "10",
            "collagen_meat_protein_ratio_100g": "10",
            "cocoa_100g": "10",
            "chlorophyl_100g": "10",
            "carbon_footprint_100g": "10",
            "carbon_footprint_from_meat_or_fish_100g": "10",
            "nutrition_score_fr_100g": "10",
            "nutrition_score_uk_100g": "10",
            "glycemic_index_100g": "10",
            "water_hardness_100g": "10",
            "choline_100g": "10",
            "phylloquinone_100g": "10",
            "beta_glucan_100g": "10",
            "inositol_100g": "10",
            "carnitine_100g": "10"
        }

        response = requests.post(url=self.endpoint_products, data=new_product)
        assert response.status_code == 201
        assert response.json()['status'] == new_product['status']

    def test_put_product(self):
        product_updated = {
            "code": "00001",
            "status": "published",
            "url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "creator": "speedy",
            "product_name": "product test put",
            "generic_name": "product",
            "quantity": "10",
            "packaging": "product",
            "packaging_tags": "product",
            "brands": "product",
            "brands_tags": "product",
            "categories": "food",
            "categories_tags": "food",
            "origins": "factory",
            "origins_tags": "factory",
            "manufacturing_places": "brazil",
            "manufacturing_places_tags": "brazil",
            "labels": "food",
            "labels_tags": "food",
            "emb_codes": "00001",
            "emb_codes_tags": "000001",
            "cities": "sp",
            "cities_tags": "sp",
            "purchase_places": "brazil",
            "stores": "brazil",
            "countries": "brazil",
            "ingredients_text": "brazil",
            "allergens": "brazil",
            "allergens_tags": "brazil",
            "traces": "brazil",
            "traces_tags": "brazil",
            "serving_size": "product",
            "serving_quantity": "product",
            "no_nutriments": "product",
            "additives_n": "product",
            "additives_tags": "product",
            "ingredients_from_palm_oil_n": "1",
            "ingredients_from_palm_oil": "1",
            "ingredients_from_palm_oil_tags": "2",
            "ingredients_that_may_be_from_palm_oil_n": "2",
            "ingredients_that_may_be_from_palm_oil": "3",
            "ingredients_that_may_be_from_palm_oil_tags": "4",
            "nutriscore_score": "10",
            "nutriscore_grade": "10",
            "nova_group": "food",
            "pnns_groups_1": "food",
            "pnns_groups_2": "food",
            "states": "sp",
            "main_category": "food",
            "image_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_small_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_front_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_front_small_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_ingredients_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_ingredients_small_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_nutrition_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "image_nutrition_small_url": "https://gutsytechster.files.wordpress.com/2019/06/cron-job-in-django.png?w=810&h=1&crop=1",
            "energy_kj_100g": "10",
            "energy_kcal_100g": "10",
            "energy_100g": "10",
            "energy_from_fat_100g": "10",
            "fat_100g": "10",
            "saturated_fat_100g": "10",
            "butyric_acid_100g": "10",
            "caproic_acid_100g": "10",
            "caprylic_acid_100g": "10",
            "capric_acid_100g": "10",
            "lauric_acid_100g": "10",
            "myristic_acid_100g": "10",
            "palmitic_acid_100g": "10",
            "stearic_acid_100g": "10",
            "arachidic_acid_100g": "10",
            "behenic_acid_100g": "10",
            "lignoceric_acid_100g": "10",
            "cerotic_acid_100g": "10",
            "montanic_acid_100g": "10",
            "melissic_acid_100g": "10",
            "monounsaturated_fat_100g": "10",
            "polyunsaturated_fat_100g": "10",
            "omega_3_fat_100g": "10",
            "alpha_linolenic_acid_100g": "10",
            "eicosapentaenoic_acid_100g": "10",
            "docosahexaenoic_acid_100g": "10",
            "omega_6_fat_100g": "10",
            "linoleic_acid_100g": "10",
            "arachidonic_acid_100g": "10",
            "gamma_linolenic_acid_100g": "10",
            "dihomo_gamma_linolenic_acid_100g": "10",
            "omega_9_fat_100g": "10",
            "oleic_acid_100g": "10",
            "elaidic_acid_100g": "10",
            "gondoic_acid_100g": "10",
            "mead_acid_100g": "10",
            "erucic_acid_100g": "10",
            "nervonic_acid_100g": "10",
            "trans_fat_100g": "10",
            "cholesterol_100g": "10",
            "carbohydrates_100g": "10",
            "sugars_100g": "10",
            "sucrose_100g": "10",
            "glucose_100g": "10",
            "fructose_100g": "10",
            "lactose_100g": "10",
            "maltose_100g": "10",
            "maltodextrins_100g": "10",
            "starch_100g": "10",
            "polyols_100g": "10",
            "fiber_100g": "10",
            "proteins_100g": "10",
            "casein_100g": "10",
            "serum_proteins_100g": "10",
            "nucleotides_100g": "10",
            "salt_100g": "10",
            "sodium_100g": "10",
            "alcohol_100g": "10",
            "vitamin_a_100g": "10",
            "beta_carotene_100g": "10",
            "vitamin_d_100g": "10",
            "vitamin_e_100g": "10",
            "vitamin_k_100g": "10",
            "vitamin_c_100g": "10",
            "vitamin_b1_100g": "10",
            "vitamin_b2_100g": "10",
            "vitamin_pp_100g": "10",
            "vitamin_b6_100g": "10",
            "vitamin_b9_100g": "10",
            "folates_100g": "10",
            "vitamin_b12_100g": "10",
            "biotin_100g": "10",
            "pantothenic_acid_100g": "10",
            "silica_100g": "10",
            "bicarbonate_100g": "10",
            "potassium_100g": "10",
            "chloride_100g": "10",
            "calcium_100g": "10",
            "phosphorus_100g": "10",
            "iron_100g": "10",
            "magnesium_100g": "10",
            "zinc_100g": "10",
            "copper_100g": "10",
            "manganese_100g": "10",
            "fluoride_100g": "10",
            "selenium_100g": "10",
            "chromium_100g": "10",
            "molybdenum_100g": "10",
            "iodine_100g": "10",
            "caffeine_100g": "10",
            "taurine_100g": "10",
            "ph_100g": "10",
            "fruits_vegetables_nuts_100g": "10",
            "fruits_vegetables_nuts_dried_100g": "10",
            "fruits_vegetables_nuts_estimate_100g": "10",
            "collagen_meat_protein_ratio_100g": "10",
            "cocoa_100g": "10",
            "chlorophyl_100g": "10",
            "carbon_footprint_100g": "10",
            "carbon_footprint_from_meat_or_fish_100g": "10",
            "nutrition_score_fr_100g": "10",
            "nutrition_score_uk_100g": "10",
            "glycemic_index_100g": "10",
            "water_hardness_100g": "10",
            "choline_100g": "10",
            "phylloquinone_100g": "10",
            "beta_glucan_100g": "10",
            "inositol_100g": "10",
            "carnitine_100g": "10"
        }

        response = requests.put(url=f'{self.endpoint_products}2/', data=product_updated)
        assert response.status_code == 200
        assert response.json()['code'] == product_updated['code']
        assert response.json()['status'] == product_updated['status']

    def test_delete_product(self):
        response = requests.delete(url=f'{self.endpoint_products}2/')
        assert response.status_code == 200