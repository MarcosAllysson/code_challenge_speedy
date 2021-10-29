# Generated by Django 3.2.8 on 2021-10-28 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250, verbose_name='code')),
                ('status', models.CharField(choices=[('draft', 'draft'), ('trash', 'trash'), ('published', 'published')], default='draft', max_length=250, verbose_name='status')),
                ('imported_t', models.DateTimeField(auto_now_add=True, verbose_name='imported')),
                ('url', models.URLField(verbose_name='url')),
                ('creator', models.CharField(max_length=250, verbose_name='creator')),
                ('created_t', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified_t', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('product_name', models.CharField(max_length=250, verbose_name='product name')),
                ('generic_name', models.CharField(max_length=250, verbose_name='generic name')),
                ('quantity', models.CharField(max_length=250, verbose_name='quantity')),
                ('packaging', models.CharField(max_length=250, verbose_name='packaging')),
                ('packaging_tags', models.TextField(verbose_name='packaging tags')),
                ('brands', models.CharField(max_length=250, verbose_name='brands')),
                ('brands_tags', models.TextField(verbose_name='brands tags')),
                ('categories', models.CharField(max_length=250, verbose_name='categories')),
                ('categories_tags', models.TextField(verbose_name='categories tags')),
                ('origins', models.CharField(max_length=250, verbose_name='origins')),
                ('origins_tags', models.TextField(verbose_name='origins tags')),
                ('manufacturing_places', models.CharField(max_length=250, verbose_name='manufacturing places')),
                ('manufacturing_places_tags', models.TextField(verbose_name='manufacturing places tags')),
                ('labels', models.CharField(max_length=250, verbose_name='labels')),
                ('labels_tags', models.TextField(verbose_name='labels tags')),
                ('emb_codes', models.CharField(max_length=250, verbose_name='emb codes')),
                ('emb_codes_tags', models.TextField(verbose_name='emb codes tags')),
                ('cities', models.CharField(max_length=250, verbose_name='cities')),
                ('cities_tags', models.TextField(verbose_name='cities tags')),
                ('purchase_places', models.CharField(max_length=250, verbose_name='purchase places')),
                ('stores', models.CharField(max_length=250, verbose_name='stores')),
                ('countries', models.CharField(max_length=250, verbose_name='countries')),
                ('ingredients_text', models.CharField(max_length=250, verbose_name='ingredients text')),
                ('allergens', models.CharField(max_length=250, verbose_name='allergens')),
                ('allergens_tags', models.TextField(verbose_name='allergens tags')),
                ('traces', models.CharField(max_length=250, verbose_name='traces')),
                ('traces_tags', models.TextField(verbose_name='traces tags')),
                ('serving_size', models.CharField(max_length=250, verbose_name='serving size')),
                ('serving_quantity', models.CharField(max_length=250, verbose_name='serving quantity')),
                ('no_nutriments', models.CharField(max_length=250, verbose_name='no nutriments')),
                ('additives_n', models.CharField(max_length=250, verbose_name='additives')),
                ('additives_tags', models.TextField(verbose_name='additives tags')),
                ('ingredients_from_palm_oil_n', models.CharField(max_length=250, verbose_name='ingredients_from_palm_oil')),
                ('ingredients_from_palm_oil', models.CharField(max_length=250, verbose_name='ingredients_from_palm_oil')),
                ('ingredients_from_palm_oil_tags', models.TextField(verbose_name='ingredients from palm oil tags')),
                ('ingredients_that_may_be_from_palm_oil_n', models.CharField(max_length=250, verbose_name='ingredients_that_may_be_from_palm_oil')),
                ('ingredients_that_may_be_from_palm_oil', models.CharField(max_length=250, verbose_name='ingredients_that_may_be_from_palm_oil')),
                ('ingredients_that_may_be_from_palm_oil_tags', models.TextField(verbose_name='ingredients_that_may_be_from_palm_oil')),
                ('nutriscore_score', models.CharField(max_length=250, verbose_name='nutriscore_score')),
                ('nutriscore_grade', models.CharField(max_length=250, verbose_name='nutriscore_grade')),
                ('nova_group', models.CharField(max_length=250, verbose_name='nova_group')),
                ('pnns_groups_1', models.CharField(max_length=250, verbose_name='pnns_groups_1')),
                ('pnns_groups_2', models.CharField(max_length=250, verbose_name='pnns_groups_2')),
                ('states', models.CharField(max_length=250, verbose_name='states')),
                ('main_category', models.CharField(max_length=250, verbose_name='main_category')),
                ('image_url', models.URLField(verbose_name='image_url')),
                ('image_small_url', models.URLField(verbose_name='image_small_url')),
                ('image_front_url', models.URLField(verbose_name='image_front_url')),
                ('image_front_small_url', models.URLField(verbose_name='image_front_small_url')),
                ('image_ingredients_url', models.URLField(verbose_name='image_ingredients_url')),
                ('image_ingredients_small_url', models.URLField(verbose_name='image_ingredients_small_url')),
                ('image_nutrition_url', models.URLField(verbose_name='image_nutrition_url')),
                ('image_nutrition_small_url', models.URLField(verbose_name='image_nutrition_small_url')),
                ('energy_kj_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='energy_kj_100g')),
                ('energy_kcal_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='energy_kcal_100g')),
                ('energy_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='energy_100g')),
                ('energy_from_fat_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='energy_from_fat_100g')),
                ('fat_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='fat_100g')),
                ('saturated_fat_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='saturated_fat_100g')),
                ('butyric_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='butyric_acid_100g')),
                ('caproic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='caproic_acid_100g')),
                ('caprylic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='caprylic_acid_100g')),
                ('capric_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='capric_acid_100g')),
                ('lauric_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='lauric_acid_100g')),
                ('myristic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='myristic_acid_100g')),
                ('palmitic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='palmitic_acid_100g')),
                ('stearic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='stearic_acid_100g')),
                ('arachidic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='arachidic_acid_100g')),
                ('behenic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='behenic_acid_100g')),
                ('lignoceric_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='lignoceric_acid_100g')),
                ('cerotic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='cerotic_acid_100g')),
                ('montanic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='montanic_acid_100g')),
                ('melissic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='melissic_acid_100g')),
                ('monounsaturated_fat_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='monounsaturated_fat_100g')),
                ('polyunsaturated_fat_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='polyunsaturated_fat_100g')),
                ('omega_3_fat_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='omega_3_fat_100g')),
                ('alpha_linolenic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='alpha_linolenic_acid_100g')),
                ('eicosapentaenoic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='eicosapentaenoic_acid_100g')),
                ('docosahexaenoic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='docosahexaenoic_acid_100g')),
                ('omega_6_fat_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='omega_6_fat_100g')),
                ('linoleic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='linoleic_acid_100g')),
                ('arachidonic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='arachidonic_acid_100g')),
                ('gamma_linolenic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='gamma_linolenic_acid_100g')),
                ('dihomo_gamma_linolenic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='dihomo_gamma_linolenic_acid_100g')),
                ('omega_9_fat_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='omega_9_fat_100g')),
                ('oleic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='oleic_acid_100g')),
                ('elaidic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='elaidic_acid_100g')),
                ('gondoic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='gondoic_acid_100g')),
                ('mead_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='mead_acid_100g')),
                ('erucic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='erucic_acid_100g')),
                ('nervonic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='nervonic_acid_100g')),
                ('trans_fat_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='trans_fat_100g')),
                ('cholesterol_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='cholesterol_100g')),
                ('carbohydrates_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='carbohydrates_100g')),
                ('sugars_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='sugars_100g')),
                ('sucrose_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='sucrose_100g')),
                ('glucose_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='glucose_100g')),
                ('fructose_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='fructose_100g')),
                ('lactose_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='lactose_100g')),
                ('maltose_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='maltose_100g')),
                ('maltodextrins_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='maltodextrins_100g')),
                ('starch_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='starch_100g')),
                ('polyols_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='polyols_100g')),
                ('fiber_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='fiber_100g')),
                ('proteins_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='proteins_100g')),
                ('casein_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='casein_100g')),
                ('serum_proteins_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='serum_proteins_100g')),
                ('nucleotides_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='nucleotides_100g')),
                ('salt_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='salt_100g')),
                ('sodium_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='sodium_100g')),
                ('alcohol_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='alcohol_100g')),
                ('vitamin_a_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='vitamin_a_100g')),
                ('beta_carotene_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='beta_carotene_100g')),
                ('vitamin_d_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='vitamin_d_100g')),
                ('vitamin_e_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='vitamin_e_100g')),
                ('vitamin_k_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='vitamin_k_100g')),
                ('vitamin_c_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='vitamin_c_100g')),
                ('vitamin_b1_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='vitamin_b1_100g')),
                ('vitamin_b2_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='vitamin_b2_100g')),
                ('vitamin_pp_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='vitamin_pp_100g')),
                ('vitamin_b6_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='vitamin_b6_100g')),
                ('vitamin_b9_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='vitamin_b9_100g')),
                ('folates_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='folates_100g')),
                ('vitamin_b12_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='vitamin_b12_100g')),
                ('biotin_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='biotin_100g')),
                ('pantothenic_acid_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='pantothenic_acid_100g')),
                ('silica_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='silica_100g')),
                ('bicarbonate_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='bicarbonate_100g')),
                ('potassium_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='potassium_100g')),
                ('chloride_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='chloride_100g')),
                ('calcium_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='calcium_100g')),
                ('phosphorus_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='phosphorus_100g')),
                ('iron_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='iron_100g')),
                ('magnesium_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='magnesium_100g')),
                ('zinc_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='zinc_100g')),
                ('copper_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='copper_100g')),
                ('manganese_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='manganese_100g')),
                ('fluoride_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='fluoride_100g')),
                ('selenium_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='selenium_100g')),
                ('chromium_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='chromium_100g')),
                ('molybdenum_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='molybdenum_100g')),
                ('iodine_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='iodine_100g')),
                ('caffeine_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='caffeine_100g')),
                ('taurine_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='taurine_100g')),
                ('ph_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='ph_100g')),
                ('fruits_vegetables_nuts_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='fruits_vegetables_nuts_100g')),
                ('fruits_vegetables_nuts_dried_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='fruits_vegetables_nuts_dried_100g')),
                ('fruits_vegetables_nuts_estimate_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='fruits_vegetables_nuts_estimate_100g')),
                ('collagen_meat_protein_ratio_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='collagen_meat_protein_ratio_100g')),
                ('cocoa_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='cocoa_100g')),
                ('chlorophyl_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='chlorophyl_100g')),
                ('carbon_footprint_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='carbon_footprint_100g')),
                ('carbon_footprint_from_meat_or_fish_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='carbon_footprint_from_meat_or_fish_100g')),
                ('nutrition_score_fr_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='nutrition_score_fr_100g')),
                ('nutrition_score_uk_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='nutrition_score_uk_100g')),
                ('glycemic_index_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='glycemic_index_100g')),
                ('water_hardness_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='water_hardness_100g')),
                ('choline_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='choline_100g')),
                ('phylloquinone_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='phylloquinone_100g')),
                ('beta_glucan_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='beta_glucan_100g')),
                ('inositol_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='inositol_100g')),
                ('carnitine_100g', models.DecimalField(decimal_places=1, default=0.0, max_digits=5, verbose_name='carnitine_100g')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['id'],
            },
        ),
    ]