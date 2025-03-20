from input.data_input import connect_db, create_table, insert_data, close_db
from output.data_output import connect_db as connect_output, fetch_data, display_data, close_db as close_output

def main():
    db_name = 'timika_pemerintah.db'
    
    # Input Data
    conn = connect_db(db_name)
    create_table(conn)
    
    # Contoh input data
    insert_data(conn, 'Budi Santoso', 'Kepala Dinas', 'Dinas Pendidikan')
    insert_data(conn, 'Siti Aminah', 'Sekretaris', 'Dinas Kesehatan')
    
    close_db(conn)

    # Output Data
    conn_output = connect_output(db_name)
    data = fetch_data(conn_output)
    display_data(data)
    close_output(conn_output)

if __name__ == '__main__':
    main()
