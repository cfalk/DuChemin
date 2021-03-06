DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'duchemin',                      # Or path to database file if using sqlite3.
        'USER': 'duchemin',                      # Not used with sqlite3.
        'PASSWORD': 'SecurePassword',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#SOLR_SERVER = "http://duchemin-dev.haverford.edu:8080/duchemin-solr"
SOLR_SERVER = "http://localhost:8080/duchemin-solr/"
VEXF_SERVER = "http://duchemin-dev.haverford.edu:8080/notation"
