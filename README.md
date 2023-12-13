# supabased
A Python Helper for Supabase Things

Setup
-----

Before running the script, make sure to set up the required environment variables: `SUPABASE_URL` and `SUPABASE_KEY_SERVICE`.

Functions
---------

### 1\. `get_env_value(key)`

*   Retrieves the value of the specified environment variable.
*   Parameters:
    *   `key`: The name of the environment variable.
*   Returns:
    *   The value of the environment variable or a default message if the variable is not found.

### 2\. `create_supabase_client() -> Client`

*   Creates and returns a Supabase client using the provided Supabase URL and service key.

### 3\. Encryption and Decryption

*   `encrypt(message: bytes, key: bytes) -> bytes`
    *   Encrypts a message using the provided key.
*   `decrypt(token: bytes, key: bytes) -> bytes`
    *   Decrypts a token using the provided key.

### 4\. `check_if_data_exists_on_supbase(supaClient, table_name, column_name, column_value)`

*   Checks if data with the specified column value exists in the specified table.
*   Parameters:
    *   `supaClient`: Supabase client.
    *   `table_name`: Name of the table.
    *   `column_name`: Name of the column.
    *   `column_value`: Value to check for.
*   Returns:
    *   `True` if data exists, `False` otherwise.

### 5\. Database Operations

#### Fetch Data

*   `fetch_data(supaClient, table_name, column_name, column_value)`
    *   Fetches data from the specified table based on column equality.
*   `fetch_data_equals_to(supaClient, table_name, column_name, column_value)`
    *   Fetches data where the column is equal to a value.
*   Additional functions for various comparison operations (`neq`, `gt`, `lt`, `gte`, `lte`, `like`, `ilike`, `is_`, `is_in`, `contains`, `contained_by`).

#### Insert, Update, Upsert, and Delete

*   `insert_data(supaClient, table_name, data)`
*   `update_data(supaClient, table_name, column_name, column_value, data)`
*   `upsert_data(supaClient, table_name, column_name, column_value, data)`
*   `delete_data(supaClient, table_name, column_name, column_value)`

#### Order and Limit

*   `fetch_data_order_the_results(supaClient, table_name, column_name, desc=True)`
*   `fetch_data_limit_the_number_of_rows_returned(supaClient, table_name, limit=1)`

#### Filter by Type

*   `fetch_data_with_filter_type(supaClient, table_name, column_name, column_value, filter_type)`

### 6\. Authentication

#### User Management

*   `create_a_new_user(supaClient, email, password)`
*   `sign_in_a_user(supaClient, email, password)`
*   `sign_in_a_user_through_otp(supaClient, email)`
*   `sign_in_a_user_through_0auth(supaClient, provider, access_token)`
*   `sign_out_a_user(supaClient, access_token)`

#### Session Management

*   `verify_and_log_in_through_otp(supaClient, email, otp)`
*   `retrieve_a_session(supaClient, access_token)`
*   `retrieve_a_new_session(supaClient, refresh_token)`
*   `retrieve_a_user(supaClient)`
*   `set_the_session_data(supaClient, access_token, refresh_token, data)`

### 7\. Storage Operations

#### Bucket Management

*   `create_a_bucket(supaClient, bucket_name)`
*   `retrieve_a_bucket(supaClient, bucket_name)`
*   `list_all_buckets(supaClient)`
*   `delete_a_bucket(supaClient, bucket_name)`
*   `empty_a_bucket(supaClient, bucket_name)`

#### File Operations

*   `upload_a_file(supaClient, bucket_name, file, path, file_options)`
*   `download_a_file(supaClient, bucket_name, source)`
*   `list_all_files_in_a_bucket(supaClient, bucket_name)`
*   `replace_an_existing_file(supaClient, bucket_name, file, path, file_options)`
*   `move_an_existing_file(supaClient, bucket_name, source, destination)`
*   `delete_files_in_a_bucket(supaClient, bucket_name, path)`

#### URL Generation

*   `create_a_signed_url(supaClient, bucket_name, filepath, expiry_duration)`
*   `retrieve_public_url(supaClient, bucket_name, filepath)`

### 8\. Function Invocation

*   `invoke_a_function(supaClient, function_name, invoke_options)`
