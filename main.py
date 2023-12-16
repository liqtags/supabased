from supabased import create_supabase_client, Client, check_if_data_exists_on_supbase, BUCKET, fetch_data_not_equals_to
from supabased import fetch_data, fetch_data_equals_to, fetch_data_with_filter_type, insert_data, fetch_data_list, base_query, filter_by_match_array

supaClient = create_supabase_client()

# define matches - mock
matches = [
    {
        "attribute": "filechain->name",
        "value": "test",
        "type": "like"
    }, 
]
            
query = base_query(supaClient, 'directory_audits')
query = filter_by_match_array(supaClient, matches, 'directory_audits')
print(query)
print(len(query.data))
        
