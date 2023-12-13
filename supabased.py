import supabase
from supabase import create_client, Client
from cryptography.fernet import Fernet
import os

def get_env_value(key):
    try:
        return os.environ[key]
    except KeyError:
        return 'there is no such key'

SUPABASE_URL = get_env_value('SUPABASE_URL')
SUPABASE_KEY_SERVICE = get_env_value('SUPABASE_KEY_SERVICE')
BUCKET = get_env_value('BUCKET')

def create_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY_SERVICE)

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

def check_if_data_exists_on_supbase(supaClient, table_name, column_name, column_value): 
    thing = supaClient.table(table_name).select("*").eq(column_name, column_value).execute()

    if len(thing.data) > 0:
        return True
    
    return False

# DATABASE
def fetch_data(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").eq(column_name, column_value).execute()
    except Exception as e:
        return e.message
    
def insert_data(supaClient, table_name, data):
    try:
        return supaClient.table(table_name).insert(data).execute()
    except Exception as e:
        return e.message
    
def update_data(supaClient, table_name, column_name, column_value, data):
    try:
        return supaClient.table(table_name).update(data).eq(column_name, column_value).execute()
    except Exception as e:
        return e.message
    
def upsert_data(supaClient, table_name, column_name, column_value, data):
    try:
        return supaClient.table(table_name).upsert(data).eq(column_name, column_value).execute()
    except Exception as e:
        return e.message
    
def delete_data(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).delete().eq(column_name, column_value).execute()
    except Exception as e:
        return e.message
    
def fetch_data_equals_to(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").eq(column_name, column_value).execute()
    except Exception as e:
        return e.message
        
def fetch_data_not_equals_to(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").neq(column_name, column_value).execute()
    except Exception as e:
        return e.message
    
def fetch_data_greater_than(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").gt(column_name, column_value).execute()
    except Exception as e:
        return e.message

# Column is greater than or equal to a value
def fetch_data_greater_than_or_equal_to(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").gte(column_name, column_value).execute()
    except Exception as e:
        return e.message
    
# Column is less than a value
def fetch_data_less_than(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").lt(column_name, column_value).execute()
    except Exception as e:
        return e.message

# Column is less than or equal to a value
def fetch_data_less_than_or_equal_to(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").lte(column_name, column_value).execute()
    except Exception as e:
        return e.message

# Column matches a pattern
def fetch_data_matches_pattern(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").like(column_name, column_value).execute()
    except Exception as e:
        return e.message

# Column matches a case-insensitive pattern
def fetch_data_matches_case_insensitive_pattern(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").ilike(column_name, column_value).execute()
    except Exception as e:
        return e.message

# Column is a value
def fetch_data_is_a_value(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").is_(column_name, column_value).execute()
    except Exception as e:
        return e.message

# Column is in an array
def fetch_data_is_in_an_array(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").is_in(column_name, column_value).execute()
    except Exception as e:
        return e.message
    
# Column contains every element in a value
def fetch_data_contains_every_element_in_a_value(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").contains(column_name, column_value).execute()
    except Exception as e:
        return e.message
    
# Contained by value
def fetch_data_contained_by_value(supaClient, table_name, column_name, column_value):
    try:
        return supaClient.table(table_name).select("*").contained_by(column_name, column_value).execute()
    except Exception as e:
        return e.message
    
# Match an associated value
def fetch_data_match_an_associated_value(supaClient, table_name, column_name, column_value):
    try:
        # TODO: fix this
        return supaClient.table(table_name).select("*").associated(column_name, column_value).execute()
    except Exception as e:
        return e.message

# Don't match the filter
def fetch_data_dont_match_the_filter(supaClient, table_name, column_name, column_value):
    try:
        # TODO: fix this
        return supaClient.table(table_name).select("*").not_.is_(column_name, column_value).execute()
    except Exception as e:
        return e.message
    
# Match the filter
def fetch_data_match_the_filter(supaClient, table_name, column_name, column_value):
    try:
        # TODO: fix this
        return supaClient.table(table_name).select("*").filter(column_name, column_value).execute()
    except Exception as e:
        return e.message

# Order the results
def fetch_data_order_the_results(supaClient, table_name, column_name, desc=True):
    try:
        return supaClient.table(table_name).select("*").order(column_name, desc).execute()
    except Exception as e:
        return e.message

# Limit the number of rows returned
def fetch_data_limit_the_number_of_rows_returned(supaClient, table_name, limit=1):
    try:
        return supaClient.table(table_name).select("*").limit(limit).execute()
    except Exception as e:
        return e.message
    
def fetch_data_with_filter_type(supaClient, table_name, column_name, column_value, filter_type):
    query = supaClient.table(table_name).select("*")

    if filter_type == 'eq':
        query.eq(column_name, column_value)
    elif filter_type == 'neq':
        query.neq(column_name, column_value)
    elif filter_type == 'gt':
        query.gt(column_name, column_value)
    elif filter_type == 'lt':
        query.lt(column_name, column_value)
    elif filter_type == 'gte':
        query.gte(column_name, column_value)
    
    try:
        return query.execute()
    except Exception as e:
        return e.message

# AUTH

# Create a new user
def create_a_new_user(supaClient, email, password):
    try:
        return supaClient.auth.sign_up(email, password)
    except Exception as e:
        return e.message
    
# Sign in a user
def sign_in_a_user(supaClient, email, password):
    try:
        return supaClient.auth.sign_in(email, password)
    except Exception as e:
        return e.message
    
# Sign in a user through OTP
def sign_in_a_user_through_otp(supaClient, email):
    try:
        return supaClient.auth.sign_in_otp(email)
    except Exception as e:
        return e.message

# Sign in a user through 0auth
def sign_in_a_user_through_0auth(supaClient, provider, access_token):
    try:
        return supaClient.auth.sign_in_with_oauth(provider, access_token)
    except Exception as e:
        return e.message

# Sign out a user
def sign_out_a_user(supaClient, access_token):
    try:
        return supaClient.auth.sign_out(access_token)
    except Exception as e:
        return e.message

# Verify and log in through OTP
def verify_and_log_in_through_otp(supaClient, email, otp):
    try:
        return supaClient.auth.verify_otp(email, otp)
    except Exception as e:
        return e.message
    
# Retrieve a session
def retrieve_a_session(supaClient, access_token):
    try:
        return supaClient.auth.get_session(access_token)
    except Exception as e:
        return e.message

# Retrieve a new session
def retrieve_a_new_session(supaClient, refresh_token):
    try:
        return supaClient.auth.refresh_access_token(refresh_token)
    except Exception as e:
        return e.message

# Retrieve a user
def retrieve_a_user(supaClient):
    try:
        return supaClient.auth.get_user()
    except Exception as e:
        return e.message
# Set the session data
def set_the_session_data(supaClient, access_token, refresh_token, data):
    try:
        return supaClient.auth.set_session_data(access_token, refresh_token, data)
    except Exception as e:
        return e.message

# Create a bucket
def create_a_bucket(supaClient, bucket_name):
    try:
        return supaClient.storage.create_bucket(bucket_name)
    except Exception as e:
        return e.message
    
def retrieve_a_bucket(supaClient, bucket_name):
    try:
        return supaClient.storage.get_bucket(bucket_name)
    except Exception as e:
        return e.message

def list_all_buckets(supaClient):
    try:
        return supaClient.storage.list_buckets()
    except Exception as e:
        return e.message

def delete_a_bucket(supaClient, bucket_name):
    try:
        return supaClient.storage.remove_bucket(bucket_name)
    except Exception as e:
        return e.message

def empty_a_bucket(supaClient, bucket_name):
    try:
        return supaClient.storage.empty_bucket(bucket_name)
    except Exception as e:
        return e.message

def upload_a_file(supaClient, bucket_name, file, path, file_options):
    try:
        return supaClient.storage.from_(bucket_name).upload(file=file, path=path, file_options=file_options)
    except Exception as e:
        return e.message

def download_a_file(supaClient, bucket_name, source):
    try:
        return supaClient.storage.from_(bucket_name).download(source)
    except Exception as e:
        return e.message

def list_all_files_in_a_bucket(supaClient, bucket_name):
    try:
        return supaClient.storage.from_(bucket_name).list()
    except Exception as e:
        return e.message
    
def replace_an_existing_file(supaClient, bucket_name, file, path, file_options):
    try:
        return supaClient.storage.from_(bucket_name).update(file=file, path=path, file_options=file_options)
    except Exception as e:
        return e.message
    
def move_an_existing_file(supaClient, bucket_name, source, destination):
    try:
        return supaClient.storage.from_(bucket_name).move(source, destination)
    except Exception as e:
        return e.message
    
def delete_files_in_a_bucket(supaClient, bucket_name, path):
    try:
        return supaClient.storage.from_(bucket_name).remove(path)
    except Exception as e:
        return e.message
    
def create_a_signed_url(supaClient, bucket_name, filepath, expiry_duration):
    try:
        return supaClient.storage.from_(bucket_name).create_signed_url(filepath, expiry_duration)
    except Exception as e:
        return e.message
    
def retrieve_public_url(supaClient, bucket_name, filepath):
    try:
        return supaClient.storage.from_(bucket_name).get_public_url(filepath)
    except Exception as e:
        return e.message

def invoke_a_function(supaClient, function_name, invoke_options):
    try:
        return supaClient.functions.invoke(function_name, invoke_options)
    except Exception as e:
        return e.message

