import os


class Login:
    login_button = "//body/div[3]/div[1]/div[1]/nav[1]/div[2]/div[2]/ul[1]/span[1]/a[1]"
    email_button = 'user-mail'
    pass_button = 'pass'
    enter_button = '//body/div[@id="register-page"]/div[1]/div[1]/div[1]/div[3]/form[1]/div[3]/p[2]/input[1]'

class Home:
    sales_button = "//body/div[@id='wrapper']/nav[@id='sidebar-wrapper']/div[1]/ul[1]/div[2]/div[2]/li[3]/a[1]"
    menu_button = "//body/div[@id='wrapper']/div[@id='page-content-wrapper']/div[@id='main']/div[6]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/select[1]"
    all_option_button = "//body/div[@id='wrapper']/div[@id='page-content-wrapper']/div[@id='main']/div[6]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/select[1]/option[2]"
    filter_button = "//body/div[@id='wrapper']/div[@id='page-content-wrapper']/div[@id='main']/div[6]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/button[1]"
    date_button = "//select[@id='date-range-combo']"
    last_week_option = "//body/div[@id='wrapper']/div[@id='page-content-wrapper']/div[@id='main']/div[6]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/select[1]/option[4]"
    download_csv = "//a[@id='export-orders-btn']"
    export = "//input[@id='submit-job']"


class Directories:
    origin = os.environ.get(r"origin_dir")
    project_destiny = os.environ.get(r"destiny_dir_project")
    csv_file_path = os.environ.get(r"file")


