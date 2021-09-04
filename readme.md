# Grant all permission to mysql specific database
CREATE USER 'vicku'@'%' IDENTIFIED BY '****';
GRANT ALL PRIVILEGES ON test_new1.* TO 'vicky'@'%' WITH GRANT OPTION;

# Create Super user 
python manage.py createsuperuser

# - Migration
# 1. First Migration it will create follwing tables:- 
python manage.py migrate

auth_group                 
auth_group_permissions     
auth_permission            
auth_user                  
auth_user_groups           
auth_user_user_permissions 
django_admin_log           
django_content_type        
django_migrations          
django_session   

# 2. After Model Creation
python manage.py makemigrations
python manage.py migrate

# 3. Create Model from table
python manage.py inspectdb student_class >> myapp/models.py





