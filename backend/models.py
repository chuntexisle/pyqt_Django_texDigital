# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DfTickerTest(models.Model):
    id = models.IntegerField(blank=True, null=True)
    tab_name = models.TextField(blank=True, null=True)
    relevance_level_tab = models.IntegerField(blank=True, null=True)
    on_landing_page = models.TextField(blank=True, null=True)
    relevance_level_landing_page = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    archive = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'df_ticker_test'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TexileAppCarbonFactor(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.CharField(max_length=20)
    factor = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'texile_app_carbon_factor'


class TexileAppChangelogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    changelog = models.CharField(max_length=10000)
    version = models.CharField(max_length=10)
    app = models.CharField(max_length=10)
    os = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'texile_app_changelogs'


class TexileAppChartUsage(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart = models.CharField(max_length=30)
    visits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'texile_app_chart_usage'


class TexileAppCustomerTable(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=10)
    deviceid = models.CharField(db_column='deviceID', max_length=40)  # Field name made lowercase.
    created_time = models.DateTimeField()
    terms = models.CharField(db_column='Terms', max_length=5)  # Field name made lowercase.
    user = models.CharField(max_length=40)
    vr = models.CharField(max_length=40)
    os = models.CharField(max_length=40)
    emailid = models.CharField(db_column='emailID', max_length=100)  # Field name made lowercase.
    first_installed_vr = models.CharField(max_length=40)
    terms_vr = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'texile_app_customer_table'


class TexileAppCustommessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'texile_app_custommessage'


class TexileAppDailyIndex(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart = models.CharField(max_length=30)
    date = models.CharField(max_length=10)
    val = models.CharField(max_length=10)
    update_time = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'texile_app_daily_index'


class TexileAppDeviceChartUsage(models.Model):
    id = models.BigAutoField(primary_key=True)
    deviceid = models.CharField(db_column='deviceID', max_length=40)  # Field name made lowercase.
    chart = models.CharField(max_length=30)
    visits = models.IntegerField()
    app = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'texile_app_device_chart_usage'


class TexileAppDevicePageClicks(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=10)
    deviceid = models.CharField(db_column='deviceID', max_length=40)  # Field name made lowercase.
    session_id = models.CharField(max_length=40)
    landing_page = models.CharField(max_length=40)
    rmi_page = models.CharField(max_length=40)
    iom_page = models.CharField(max_length=40)
    t_page = models.CharField(max_length=40)
    pmf_page = models.CharField(max_length=40)
    smf_page = models.CharField(max_length=40)
    rc_page = models.CharField(max_length=40)
    wc_page = models.CharField(max_length=40)
    carbon_offset = models.CharField(max_length=40)
    watchlist = models.CharField(max_length=40)
    feedback = models.CharField(max_length=40)
    about = models.CharField(max_length=40)
    tutorial = models.CharField(max_length=40)
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'texile_app_device_page_clicks'


class TexileAppDeviceSessionChartUsage(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=10)
    deviceid = models.CharField(db_column='deviceID', max_length=40)  # Field name made lowercase.
    session_id = models.CharField(max_length=40)
    chart = models.CharField(max_length=30)
    visits = models.IntegerField()
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'texile_app_device_session_chart_usage'


class TexileAppEmails(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=200)
    archive = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'texile_app_emails'


class TexileAppFeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    deviceid = models.CharField(db_column='deviceID', max_length=300)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300)  # Field name made lowercase.
    email = models.CharField(max_length=300)
    phoneno = models.CharField(db_column='PhoneNo', max_length=10)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=1000)  # Field name made lowercase.
    rating = models.CharField(db_column='Rating', max_length=2)  # Field name made lowercase.
    app = models.CharField(max_length=10)
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'texile_app_feedback'


class TexileAppFutureYahooData(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart = models.CharField(max_length=10)
    data = models.CharField(max_length=10)
    date = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'texile_app_future_yahoo_data'


class TexileAppHourlyIndex(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart = models.CharField(max_length=30)
    date = models.CharField(max_length=10)
    val = models.CharField(max_length=10)
    update_time = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'texile_app_hourly_index'


class TexileAppHourlyYahooData(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart = models.CharField(max_length=30)
    date = models.CharField(max_length=10)
    val = models.CharField(max_length=10)
    update_time = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'texile_app_hourly_yahoo_data'


class TexileAppIndexData(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart = models.CharField(max_length=20)
    data = models.CharField(max_length=10)
    date = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'texile_app_index_data'


class TexileAppIndexDucData(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=10)
    anadarko_d = models.CharField(db_column='Anadarko_D', max_length=20)  # Field name made lowercase.
    anadarko_c = models.CharField(db_column='Anadarko_C', max_length=20)  # Field name made lowercase.
    anadarko_duc = models.CharField(db_column='Anadarko_DUC', max_length=20)  # Field name made lowercase.
    appalachia_d = models.CharField(db_column='Appalachia_D', max_length=20)  # Field name made lowercase.
    appalachia_c = models.CharField(db_column='Appalachia_C', max_length=20)  # Field name made lowercase.
    appalachia_duc = models.CharField(db_column='Appalachia_DUC', max_length=20)  # Field name made lowercase.
    bakken_d = models.CharField(db_column='Bakken_D', max_length=20)  # Field name made lowercase.
    bakken_c = models.CharField(db_column='Bakken_C', max_length=20)  # Field name made lowercase.
    bakken_duc = models.CharField(db_column='Bakken_DUC', max_length=20)  # Field name made lowercase.
    eagle_d = models.CharField(db_column='Eagle_D', max_length=20)  # Field name made lowercase.
    eagle_c = models.CharField(db_column='Eagle_C', max_length=20)  # Field name made lowercase.
    eagle_duc = models.CharField(db_column='Eagle_DUC', max_length=20)  # Field name made lowercase.
    haynesville_d = models.CharField(db_column='Haynesville_D', max_length=20)  # Field name made lowercase.
    haynesville_c = models.CharField(db_column='Haynesville_C', max_length=20)  # Field name made lowercase.
    haynesville_duc = models.CharField(db_column='Haynesville_DUC', max_length=20)  # Field name made lowercase.
    niobrara_d = models.CharField(db_column='Niobrara_D', max_length=20)  # Field name made lowercase.
    niobrara_c = models.CharField(db_column='Niobrara_C', max_length=20)  # Field name made lowercase.
    niobrara_duc = models.CharField(db_column='Niobrara_DUC', max_length=20)  # Field name made lowercase.
    permian_d = models.CharField(db_column='Permian_D', max_length=20)  # Field name made lowercase.
    permian_c = models.CharField(db_column='Permian_C', max_length=20)  # Field name made lowercase.
    permian_duc = models.CharField(db_column='Permian_DUC', max_length=20)  # Field name made lowercase.
    dpr_d = models.CharField(db_column='DPR_D', max_length=20)  # Field name made lowercase.
    dpr_c = models.CharField(db_column='DPR_C', max_length=20)  # Field name made lowercase.
    dpr_duc = models.CharField(db_column='DPR_DUC', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'texile_app_index_duc_data'


class TexileAppIndexFData(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=10)
    ho = models.CharField(db_column='HO', max_length=20)  # Field name made lowercase.
    rb = models.CharField(db_column='RB', max_length=20)  # Field name made lowercase.
    f_index = models.CharField(db_column='F_index', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'texile_app_index_f_data'


class TexileAppIndexIomData(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=10)
    rio = models.CharField(db_column='RIO', max_length=20)  # Field name made lowercase.
    vale = models.CharField(db_column='VALE', max_length=20)  # Field name made lowercase.
    sxc = models.CharField(db_column='SXC', max_length=20)  # Field name made lowercase.
    bhp = models.CharField(db_column='BHP', max_length=20)  # Field name made lowercase.
    iom_index = models.CharField(db_column='IOM_index', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'texile_app_index_iom_data'


class TexileAppIndexPmfData(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=10)
    ts = models.CharField(db_column='TS', max_length=20)  # Field name made lowercase.
    vkpa = models.CharField(db_column='VKPA', max_length=20)  # Field name made lowercase.
    x = models.CharField(db_column='X', max_length=20)  # Field name made lowercase.
    tmst = models.CharField(db_column='TMST', max_length=20)  # Field name made lowercase.
    nwpx = models.CharField(db_column='NWPX', max_length=20)  # Field name made lowercase.
    pmf_index = models.CharField(db_column='PMF_index', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'texile_app_index_pmf_data'


class TexileAppIndexRigData(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=10)
    ardmore = models.CharField(db_column='Ardmore', max_length=20)  # Field name made lowercase.
    arkoma = models.CharField(db_column='Arkoma', max_length=20)  # Field name made lowercase.
    barnett = models.CharField(db_column='Barnett', max_length=20)  # Field name made lowercase.
    cana = models.CharField(db_column='Cana', max_length=20)  # Field name made lowercase.
    niobrara = models.CharField(db_column='Niobrara', max_length=20)  # Field name made lowercase.
    ford = models.CharField(db_column='Ford', max_length=20)  # Field name made lowercase.
    granite = models.CharField(db_column='Granite', max_length=20)  # Field name made lowercase.
    haynesville = models.CharField(db_column='Haynesville', max_length=20)  # Field name made lowercase.
    marcellus = models.CharField(db_column='Marcellus', max_length=20)  # Field name made lowercase.
    mississippian = models.CharField(db_column='Mississippian', max_length=20)  # Field name made lowercase.
    permian = models.CharField(db_column='Permian', max_length=20)  # Field name made lowercase.
    utica = models.CharField(db_column='Utica', max_length=20)  # Field name made lowercase.
    williston = models.CharField(db_column='Williston', max_length=20)  # Field name made lowercase.
    rc_index = models.CharField(db_column='RC_index', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'texile_app_index_rig_data'


class TexileAppIndexRmiCmeData(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=10)
    scrap = models.CharField(db_column='SCRAP', max_length=20)  # Field name made lowercase.
    hrc = models.CharField(db_column='HRC', max_length=20)  # Field name made lowercase.
    coal = models.CharField(db_column='COAL', max_length=20)  # Field name made lowercase.
    ironore = models.CharField(db_column='IRONORE', max_length=20)  # Field name made lowercase.
    rmi_index = models.CharField(db_column='RMI_index', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'texile_app_index_rmi_cme_data'


class TexileAppIndexRmiData(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=10)
    scrap = models.CharField(db_column='SCRAP', max_length=20)  # Field name made lowercase.
    hrc = models.CharField(db_column='HRC', max_length=20)  # Field name made lowercase.
    coal = models.CharField(db_column='COAL', max_length=20)  # Field name made lowercase.
    ironore = models.CharField(db_column='IRONORE', max_length=20)  # Field name made lowercase.
    rmi_index = models.CharField(db_column='RMI_index', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'texile_app_index_rmi_data'


class TexileAppIndexSmfData(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=10)
    mt = models.CharField(db_column='MT', max_length=20)  # Field name made lowercase.
    pkx = models.CharField(db_column='PKX', max_length=20)  # Field name made lowercase.
    nue = models.CharField(db_column='NUE', max_length=20)  # Field name made lowercase.
    stld = models.CharField(db_column='STLD', max_length=20)  # Field name made lowercase.
    rs = models.CharField(db_column='RS', max_length=20)  # Field name made lowercase.
    clf = models.CharField(db_column='CLF', max_length=20)  # Field name made lowercase.
    tx = models.CharField(db_column='TX', max_length=20)  # Field name made lowercase.
    ggb = models.CharField(db_column='GGB', max_length=20)  # Field name made lowercase.
    x = models.CharField(db_column='X', max_length=20)  # Field name made lowercase.
    cmc = models.CharField(db_column='CMC', max_length=20)  # Field name made lowercase.
    tkade = models.CharField(db_column='TKADE', max_length=20)  # Field name made lowercase.
    szgde = models.CharField(db_column='SZGDE', max_length=20)  # Field name made lowercase.
    nippon = models.CharField(db_column='NIPPON', max_length=20)  # Field name made lowercase.
    jfe = models.CharField(db_column='JFE', max_length=20)  # Field name made lowercase.
    smf_index = models.CharField(db_column='SMF_index', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'texile_app_index_smf_data'


class TexileAppIndexTData(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=10)
    ulsd = models.CharField(db_column='ULSD', max_length=20)  # Field name made lowercase.
    baltic = models.CharField(db_column='BALTIC', max_length=20)  # Field name made lowercase.
    allgrade = models.CharField(db_column='ALLGRADE', max_length=20)  # Field name made lowercase.
    t_index = models.CharField(db_column='T_index', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'texile_app_index_t_data'


class TexileAppMarketCapData(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart = models.CharField(max_length=20)
    data = models.CharField(max_length=10)
    date = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'texile_app_market_cap_data'


class TexileAppNews(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    website = models.CharField(max_length=1000)
    date = models.DateTimeField()
    image = models.TextField()
    chart = models.CharField(max_length=200)
    relevance_level = models.IntegerField()
    archive = models.CharField(max_length=1)
    word_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'texile_app_news'


class TexileAppNewsData(models.Model):
    id = models.BigAutoField(primary_key=True)
    tab_name = models.CharField(max_length=20)
    relevance_level_tab = models.IntegerField()
    on_landing_page = models.CharField(max_length=1)
    relevance_level_landing_page = models.IntegerField()
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    website = models.CharField(max_length=1000)
    date = models.DateTimeField()
    image = models.TextField()
    archive = models.CharField(max_length=1)
    word_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'texile_app_news_data'


class TexileAppNewsDataTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    tab_name = models.CharField(max_length=20)
    relevance_level_tab = models.IntegerField()
    on_landing_page = models.CharField(max_length=1)
    relevance_level_landing_page = models.IntegerField()
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    website = models.CharField(max_length=1000)
    date = models.DateTimeField()
    image = models.TextField()
    archive = models.CharField(max_length=1)
    word_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'texile_app_news_data_test'


class TexileAppNewsRec(models.Model):
    id = models.BigAutoField(primary_key=True)
    tab_name = models.CharField(max_length=20)
    relevance_level_tab = models.IntegerField()
    on_landing_page = models.CharField(max_length=1)
    relevance_level_landing_page = models.IntegerField()
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    website = models.CharField(max_length=1000)
    date = models.DateTimeField()
    image = models.TextField()
    archive = models.CharField(max_length=1)
    exp_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'texile_app_news_rec'


class TexileAppNewsTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart = models.CharField(max_length=200)
    relevance_level = models.IntegerField()
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    website = models.CharField(max_length=1000)
    date = models.DateTimeField()
    image = models.TextField()
    archive = models.CharField(max_length=1)
    word_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'texile_app_news_test'


class TexileAppReleasedLots(models.Model):
    lot_number = models.IntegerField(primary_key=True)
    qty_uv_coated = models.IntegerField(blank=True, null=True)
    qty_nouv_coating = models.IntegerField(blank=True, null=True)
    feet = models.FloatField(blank=True, null=True)
    tons = models.FloatField(blank=True, null=True)
    tds_transaction_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'texile_app_released_lots'


class TexileAppRmiData(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart = models.CharField(max_length=20)
    data = models.CharField(max_length=10)
    date = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'texile_app_rmi_data'


class TexileAppSessionPageUsage(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=10)
    session_id = models.CharField(max_length=40)
    landing_page = models.CharField(max_length=40)
    rmi_page = models.CharField(max_length=40)
    iom_page = models.CharField(max_length=40)
    t_page = models.CharField(max_length=40)
    pmf_page = models.CharField(max_length=40)
    smf_page = models.CharField(max_length=40)
    carbon_offset = models.CharField(max_length=40)
    deviceid = models.CharField(db_column='deviceID', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'texile_app_session_page_usage'


class TexileAppSessionPageUsageNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=10)
    deviceid = models.CharField(db_column='deviceID', max_length=40)  # Field name made lowercase.
    session_id = models.CharField(max_length=40)
    landing_page = models.CharField(max_length=40)
    rmi_page = models.CharField(max_length=40)
    iom_page = models.CharField(max_length=40)
    t_page = models.CharField(max_length=40)
    pmf_page = models.CharField(max_length=40)
    smf_page = models.CharField(max_length=40)
    carbon_offset = models.CharField(max_length=40)
    watchlist = models.CharField(max_length=40)
    feedback = models.CharField(max_length=40)
    about = models.CharField(max_length=40)
    tutorial = models.CharField(max_length=40)
    rc_page = models.CharField(max_length=40)
    wc_page = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'texile_app_session_page_usage_new'


class TexileAppSessionUsage(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=10)
    session_id = models.CharField(max_length=40)
    time = models.CharField(max_length=40)
    created_time = models.DateTimeField()
    deviceid = models.CharField(db_column='deviceID', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'texile_app_session_usage'


class TexileAppStockData(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart_type = models.CharField(max_length=20)
    data = models.FloatField()
    current = models.FloatField()

    class Meta:
        managed = False
        db_table = 'texile_app_stock_data'


class TexileAppTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    tab_name = models.CharField(max_length=10)
    relevance_level_tab = models.IntegerField()
    on_landing_page = models.CharField(max_length=1)
    relevance_level_landing_page = models.IntegerField()
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    website = models.CharField(max_length=100)
    date = models.DateTimeField()
    image = models.TextField()
    archive = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'texile_app_test'


class TexileAppTestqt(models.Model):
    tds_transaction_id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    customer = models.CharField(max_length=45, blank=True, null=True)
    gt_pipo_po = models.IntegerField(blank=True, null=True)
    processing_order = models.IntegerField(blank=True, null=True)
    wonumber = models.CharField(max_length=45, blank=True, null=True)
    od = models.FloatField(blank=True, null=True)
    wall = models.FloatField(blank=True, null=True)
    weight_per_ft = models.FloatField(blank=True, null=True)
    grade = models.CharField(max_length=45, blank=True, null=True)
    design = models.CharField(max_length=45, blank=True, null=True)
    manufacturer = models.CharField(max_length=45, blank=True, null=True)
    avg_length = models.FloatField(blank=True, null=True)
    totalqty_uv_coated = models.IntegerField(blank=True, null=True)
    totalqty_nouv_coating = models.IntegerField(blank=True, null=True)
    totalfeet = models.FloatField(blank=True, null=True)
    totaltons = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'texile_app_testqt'


class TexileAppTickerTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    tab_name = models.CharField(max_length=10)
    relevance_level_tab = models.IntegerField()
    on_landing_page = models.CharField(max_length=1)
    relevance_level_landing_page = models.IntegerField()
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    website = models.CharField(max_length=100)
    date = models.DateTimeField()
    image = models.TextField()
    archive = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'texile_app_ticker_test'


class TexileAppTransportationData(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart = models.CharField(max_length=20)
    data = models.CharField(max_length=10)
    date = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'texile_app_transportation_data'


class TexileAppTweetTableIndex(models.Model):
    id = models.BigAutoField(primary_key=True)
    tweet_link = models.CharField(max_length=100)
    html = models.TextField()
    author_name = models.TextField()
    author_url = models.TextField()
    profile_pic = models.TextField()
    image_url = models.TextField()
    web_url = models.TextField()
    web_url_image = models.TextField()
    web_text = models.TextField()
    date = models.DateTimeField()
    chart = models.CharField(max_length=200)
    relevance_level = models.IntegerField()
    archive = models.CharField(max_length=1)
    word_count = models.IntegerField()
    actual_relevant = models.CharField(max_length=2)
    predicted_relevant = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'texile_app_tweet_table_index'


class TexileAppTweetTableIndexTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    tweet_link = models.CharField(max_length=100)
    html = models.TextField()
    author_name = models.TextField()
    author_url = models.TextField()
    profile_pic = models.TextField()
    image_url = models.TextField()
    web_url = models.TextField()
    web_url_image = models.TextField()
    web_text = models.TextField()
    date = models.DateTimeField()
    chart = models.CharField(max_length=200)
    relevance_level = models.IntegerField()
    archive = models.CharField(max_length=1)
    word_count = models.IntegerField()
    actual_relevant = models.CharField(max_length=2)
    predicted_relevant = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'texile_app_tweet_table_index_test'


class TexileAppTweetTableTicker(models.Model):
    id = models.BigAutoField(primary_key=True)
    tweet_link = models.CharField(max_length=100)
    html = models.TextField()
    author_name = models.TextField()
    author_url = models.TextField()
    profile_pic = models.TextField()
    image_url = models.TextField()
    web_url = models.TextField()
    web_url_image = models.TextField()
    web_text = models.TextField()
    date = models.DateTimeField()
    tab_name = models.CharField(max_length=20)
    relevance_level_tab = models.IntegerField()
    on_landing_page = models.CharField(max_length=1)
    relevance_level_landing_page = models.IntegerField()
    archive = models.CharField(max_length=1)
    word_count = models.IntegerField()
    actual_relevant = models.CharField(max_length=2)
    predicted_relevant = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'texile_app_tweet_table_ticker'


class TexileAppTweetTableTickerTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    tweet_link = models.CharField(max_length=100)
    html = models.TextField()
    author_name = models.TextField()
    author_url = models.TextField()
    profile_pic = models.TextField()
    image_url = models.TextField()
    web_url = models.TextField()
    web_url_image = models.TextField()
    web_text = models.TextField()
    date = models.DateTimeField()
    tab_name = models.CharField(max_length=20)
    relevance_level_tab = models.IntegerField()
    on_landing_page = models.CharField(max_length=1)
    relevance_level_landing_page = models.IntegerField()
    archive = models.CharField(max_length=1)
    word_count = models.IntegerField()
    actual_relevant = models.CharField(max_length=2)
    predicted_relevant = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'texile_app_tweet_table_ticker_test'


class TexileAppUpdatedTime(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart = models.CharField(max_length=30)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'texile_app_updated_time'


class TexileAppVersionInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.CharField(max_length=10)
    app = models.CharField(max_length=10)
    url = models.CharField(max_length=100)
    os = models.CharField(max_length=20)
    terms_vr = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'texile_app_version_info'


class TexileAppWatchlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    deviceid = models.CharField(db_column='deviceID', max_length=300)  # Field name made lowercase.
    created_time = models.DateTimeField()
    config = models.TextField()
    app = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'texile_app_watchlist'


class TexileAppWebsiteViewers(models.Model):
    id = models.BigAutoField(primary_key=True)
    email_id = models.CharField(max_length=300)
    created_time = models.DateTimeField()
    config = models.TextField()

    class Meta:
        managed = False
        db_table = 'texile_app_website_viewers'


class TexileAppYDataTs(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart_type = models.CharField(max_length=10)
    data = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'texile_app_y_data_ts'


class TexileAppYahooData(models.Model):
    id = models.BigAutoField(primary_key=True)
    chart = models.CharField(max_length=10)
    chart_type = models.CharField(max_length=10)
    data = models.CharField(max_length=10)
    date = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'texile_app_yahoo_data'
