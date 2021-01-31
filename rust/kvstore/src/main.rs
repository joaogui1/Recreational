use std::collections::HashMap;
fn main() {
    let mut args = std::env::args().skip(1);
    let key = args.next().expect("No key provided");
    let value = args.next().unwrap();
    println!("The key is {} and the value is {}", key, value);
    let contents = format!("{}\t{}\n", key, value);
    std::fs::write("kv.db", contents).unwrap();

    let database = Database::new().expect("Creating db failed");
}

struct Database{
    map: HashMap<String, String>,
}

impl Database{
    fn new() -> Result<Database, std::io::Error>{
        let mut map = HashMap::new();
        let contents = std::fs::read_to_string("kv.db")?;
        for line in contents.lines(){
            let mut chunks = line.splitn(1, '\t');
            let key = chunks.next().expect("No Key!");
            let value = chunks.next().expect("No Value!");
            map.insert(key.to_owned(), value.to_owned());

        }

        Ok(Database{map: map})
    }
}
