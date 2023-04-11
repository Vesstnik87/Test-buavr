# Generated by Django 4.1.7 on 2023-04-11 04:40

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import lk.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deffect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deffect', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Diametr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_gazopr', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gazopr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gazopr', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hron', models.CharField(blank=True, max_length=255, null=True, verbose_name='Хронические заболевания')),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Местоположение')),
                ('slug', models.SlugField()),
                ('dop_1', models.CharField(blank=True, max_length=150, null=True, verbose_name='доп1')),
                ('dop_2', models.CharField(blank=True, max_length=150, null=True, verbose_name='доп2')),
                ('dop_3', models.CharField(blank=True, max_length=150, null=True, verbose_name='доп3')),
                ('dop_4', models.CharField(blank=True, max_length=150, null=True, verbose_name='доп4')),
                ('dop_5', models.CharField(blank=True, max_length=150, null=True, verbose_name='доп5')),
            ],
        ),
        migrations.CreateModel(
            name='Lpumg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lpumg', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Metod_remonta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('met_remont', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Otdel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otdel', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('name_2', models.CharField(max_length=255, verbose_name='Имя')),
                ('name_3', models.CharField(max_length=255, verbose_name='Отчество')),
                ('bithday', models.DateField(null=True, verbose_name='Дата рождения')),
                ('ustroen', models.DateField(verbose_name='Дата трудоустройства')),
                ('tabnumber', models.IntegerField(verbose_name='Табельный номер')),
                ('lvl', models.IntegerField(null=True, verbose_name='Разряд')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from=lk.models.instance_slug, slugify=lk.models.slugify_value, unique=True, verbose_name='URL')),
                ('examen_ot', models.DateField(blank=True, null=True, verbose_name='Проверка знаний по ОТ')),
                ('next_examen_ot', models.DateField(blank=True, null=True, verbose_name='Проверка знаний по ОТ')),
                ('examen_eb', models.DateField(blank=True, null=True, verbose_name='Проверка знаний по ЭБ')),
                ('next_examen_eb', models.DateField(blank=True, null=True, verbose_name='Проверка знаний по ЭБ')),
                ('examen_ptm', models.DateField(blank=True, null=True, verbose_name='ПТМ')),
                ('next_examen_ptm', models.DateField(blank=True, null=True, verbose_name='ПТМ')),
                ('examen_pdd', models.DateField(blank=True, null=True, verbose_name='ПДД')),
                ('next_examen_pdd', models.DateField(blank=True, null=True, verbose_name='ПДД')),
                ('instructaj', models.DateField(blank=True, null=True, verbose_name='Инструктаж')),
                ('med_osmotr', models.DateField(blank=True, null=True, verbose_name='Мед.осмотр')),
                ('flura', models.DateField(blank=True, null=True, verbose_name='Флюорография')),
                ('otpusk_start', models.DateField(blank=True, null=True, verbose_name='Осн.отпуск')),
                ('otpusk_end', models.DateField(blank=True, null=True, verbose_name='Осн.отпуск')),
                ('otpusk_d1_start', models.DateField(blank=True, null=True, verbose_name='Доп.отпуск')),
                ('otpusk_d1_end', models.DateField(blank=True, null=True, verbose_name='Доп.отпуск')),
                ('otpusk_d2_start', models.DateField(blank=True, null=True, verbose_name='Доп.отпуск')),
                ('otpusk_d2_end', models.DateField(blank=True, null=True, verbose_name='Доп.отпуск')),
                ('location_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Местоположение 1')),
                ('location_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Местоположение 2')),
                ('foto', models.ImageField(blank=True, help_text='150х150', null=True, upload_to='avatar/', verbose_name='Фото сотрудника')),
                ('gruppa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lk.group', verbose_name='Подразделение')),
                ('hron', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lk.hron', verbose_name='Хронические заболевания')),
                ('otdeleniye', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lk.otdel', verbose_name='Отделение')),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонал',
                'ordering': ['name_1', 'name_2'],
            },
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Этап работ')),
            ],
        ),
        migrations.CreateModel(
            name='Svarshov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Сварной шев')),
            ],
        ),
        migrations.CreateModel(
            name='Uchavr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uchavr', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Uchastok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_prikaz', models.FileField(null=True, upload_to='', verbose_name='prikaz/')),
                ('prikaz_number', models.CharField(max_length=100, null=True, verbose_name='№ совместного приказа')),
                ('prikaz_date', models.DateField(null=True, verbose_name='Дата совместного приказа')),
                ('file_razresh', models.FileField(null=True, upload_to='', verbose_name='razreshenie/')),
                ('razresh_number', models.CharField(max_length=100, null=True, verbose_name='№ разрешения')),
                ('razresh_date', models.DateField(null=True, verbose_name='Дата разрешения')),
                ('start_uch', models.FloatField(null=True, verbose_name='Начало участка')),
                ('end_uch', models.FloatField(null=True, verbose_name='Конец участка')),
                ('status_uch', models.BooleanField(blank=True, default=False, verbose_name='Статус участка')),
                ('date_start_razresh', models.DateField(null=True, verbose_name='Дата начала')),
                ('date_end_razresh', models.DateField(null=True, verbose_name='Дата окончания')),
                ('date_start_plan', models.DateField(null=True, verbose_name='Дата начала')),
                ('date_end_plan', models.DateField(null=True, verbose_name='Дата начала')),
                ('kol_trub_plan', models.IntegerField(null=True, verbose_name='Кол. труб по плану')),
                ('kol_trub_fakt', models.IntegerField(null=True, verbose_name='Кол. труб по факту')),
                ('date_start_fact', models.DateField(null=True, verbose_name='Дата начала по факту')),
                ('date_end_fact', models.DateField(null=True, verbose_name='Дата окончания по факту')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=100, null=True, populate_from=lk.models.instance_slug, slugify=lk.models.slugify_value, unique=True, verbose_name='URL')),
                ('distant_location', models.BooleanField(verbose_name='Отдаленный участок')),
                ('davleniye', models.BooleanField(default=False, verbose_name='Участок сниженного давления')),
                ('dlina_uchastka', models.FloatField(blank=True, null=True, verbose_name='Длина участка')),
                ('d_gazopr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lk.diametr', verbose_name='Диаметр газопровода')),
                ('lpu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lk.lpumg', verbose_name='Наименование филиала ЛПУМГ')),
                ('nitka', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lk.gazopr', verbose_name='Наименование газопровода')),
            ],
            options={
                'verbose_name': 'Участок',
                'verbose_name_plural': 'Участки',
                'ordering': ['nitka', 'start_uch', 'end_uch'],
            },
        ),
        migrations.CreateModel(
            name='Truba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='Номер трубы')),
                ('dlina', models.FloatField(blank=True, null=True, verbose_name='Длина трубы')),
                ('stenka', models.FloatField(blank=True, null=True, verbose_name='Толщина стенки')),
                ('construkciya', models.CharField(blank=True, max_length=50, null=True, verbose_name='Конструкция трубы')),
                ('int_psh', models.CharField(blank=True, max_length=100, null=True, verbose_name='Входящий ПШ')),
                ('out_psh', models.CharField(blank=True, max_length=100, null=True, verbose_name='Исходящий ПШ')),
                ('otvod', models.BooleanField(blank=True, verbose_name='Отвод')),
                ('otvod_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип отвода')),
                ('otvod_segment', models.IntegerField(blank=True, null=True, verbose_name='Число сегментов отвода')),
                ('otvod_izgib', models.FloatField(blank=True, null=True, verbose_name='Угол изгиба в Град.')),
                ('otvod_proekciya', models.CharField(blank=True, max_length=100, null=True, verbose_name='Угол в проекции Град.')),
                ('otvod_napravleniye', models.CharField(blank=True, max_length=100, null=True, verbose_name='Направление')),
                ('danger', models.CharField(blank=True, max_length=50, null=True, verbose_name='Опасность')),
                ('dop_8734653748', models.CharField(blank=True, max_length=150, null=True, verbose_name='дополнительное поле')),
                ('def_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Вид деффекта')),
                ('def_1_type_rem', models.CharField(blank=True, max_length=255, null=True, verbose_name='Метод ремонта')),
                ('def_1_compl_rem', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('def_1_dop_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_1_dop_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_1_dop_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_1_dop_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_1_dop_5', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_1_dop_6', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_1_dop_7', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_1_dop_8', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_1_dop_9', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_1_dop_10', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_1_percent', models.IntegerField(blank=True, null=True, verbose_name='Процент дефекта')),
                ('def_1_piket', models.FloatField(blank=True, null=True, verbose_name='Пикетаж')),
                ('def_1_km', models.FloatField(blank=True, null=True, verbose_name='Километр')),
                ('def_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Вид деффекта')),
                ('def_2_type_rem', models.CharField(blank=True, max_length=255, null=True, verbose_name='Метод ремонта')),
                ('def_2_compl_rem', models.CharField(blank=True, max_length=255, null=True, verbose_name='Метод ремонта')),
                ('def_2_dop_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_2_dop_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_2_dop_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_2_dop_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_2_dop_5', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_2_dop_6', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_2_dop_7', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_2_dop_8', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_2_dop_9', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_2_dop_10', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительное поле')),
                ('def_2_percent', models.IntegerField(blank=True, null=True, verbose_name='Процент дефекта')),
                ('def_2_piket', models.FloatField(blank=True, null=True, verbose_name='Пикетаж')),
                ('def_2_km', models.FloatField(blank=True, null=True, verbose_name='Километр')),
                ('zaglushka_sever', models.BooleanField(blank=True, default=False, verbose_name='Заглашка с северной стороны')),
                ('zaglushka_ug', models.BooleanField(blank=True, default=False, verbose_name='Заглушка с южной стороны')),
                ('peremichka_up', models.BooleanField(blank=True, default=False, verbose_name='Перемычка вверх')),
                ('peremichka_down', models.BooleanField(blank=True, default=False, verbose_name='Перемычка вниз')),
                ('comment_1', models.TextField(blank=True, max_length=100, null=True, verbose_name='Комментарий')),
                ('comment_2', models.TextField(blank=True, max_length=30, null=True, verbose_name='Комментарий')),
                ('comment_3', models.TextField(blank=True, max_length=30, null=True, verbose_name='Комментарий')),
                ('uch_trubid', models.IntegerField(blank=True, null=True)),
                ('trump_url', autoslug.fields.AutoSlugField(editable=False, max_length=100, null=True, populate_from=lk.models.instance_slug, slugify=lk.models.slugify_value, unique=True, verbose_name='trump.url')),
                ('stage_works', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lk.status', verbose_name='Этап работ')),
                ('uch_trub', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='lk.uchastok', verbose_name='Принадлежность к участку')),
            ],
            options={
                'verbose_name': 'Труба',
                'verbose_name_plural': 'Трубы',
                'ordering': ['number', 'uch_trub'],
            },
        ),
        migrations.CreateModel(
            name='Tehnika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, null=True, verbose_name='Модель техники')),
                ('gos_number', models.SlugField(max_length=100, null=True, verbose_name='Гос.номер')),
                ('icon', models.CharField(max_length=100, null=True, verbose_name='Изображение')),
                ('status', models.CharField(max_length=155, null=True, verbose_name='Статус')),
                ('location1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Местоположение 1')),
                ('location2', models.IntegerField(blank=True, null=True, verbose_name='Труба')),
                ('type', models.CharField(max_length=255, verbose_name='Тип техники')),
                ('rashod_h', models.FloatField(blank=True, null=True, verbose_name='Расход ч.')),
                ('rashod_km', models.FloatField(blank=True, null=True, verbose_name='Расход км.')),
                ('prinadlejnost', models.CharField(blank=True, max_length=100, null=True, verbose_name='Принадлежность')),
                ('inv_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Инв.номер')),
                ('teh_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Резервное поле')),
                ('teh_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Резервное поле')),
                ('teh_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Резервное поле')),
                ('teh_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Резервное поле')),
                ('teh_5', models.CharField(blank=True, max_length=255, null=True, verbose_name='Резервное поле')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lk.personal', verbose_name='Водитель')),
            ],
            options={
                'verbose_name': 'Техника',
                'verbose_name_plural': 'Техника',
                'ordering': ['type', 'model', 'gos_number', 'status', 'location1', 'location2', 'rashod_h', 'rashod_km'],
            },
        ),
        migrations.CreateModel(
            name='RabTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_finish', models.TimeField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lk.tehnika', verbose_name='Техника')),
            ],
        ),
        migrations.AddField(
            model_name='personal',
            name='professiya',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lk.prof', verbose_name='Профессия'),
        ),
        migrations.AddField(
            model_name='personal',
            name='uch_avr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lk.uchavr', verbose_name='Участок'),
        ),
    ]
