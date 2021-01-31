use std::collections::HashMap;
fn main() {
    let mut args = std::env::args().skip(1);
    let key = args.next().expect("No key provided");
    let value = args.next().unwrap();
    println!("The key is {} and the value is {}", key, value);

    let mut database = Database::new().expect("Creating db failed");
    database.insert(key.to_uppercase(), value.clone());
    database.insert(key, value);
    database.flush().unwrap();
}

struct Database{
    map: HashMap<String, String>,
    flushed: bool,
}

impl Database{
    fn new() -> Result<Database, std::io::Error>{
        let mut map = HashMap::new();
        let contents = std::fs::read_to_string("kv.db")?;
        for line in contents.lines(){
            let mut chunks = line.splitn(2, '\t');
            let key = chunks.next().expect("No Key!");
            let value = chunks.next().expect("No Value!");
            map.insert(key.to_owned(), value.to_owned());
        }

        Ok(Database{map, flushed: false})
    }

    fn insert(&mut self, key:String , value: String){
        self.map.insert(key, value);
    }

    fn flush(mut self) -> std::io::Result<()>{
        self.flushed = true;
        flush(&self)
    }
}

impl Drop for Database{
    fn drop(&mut self){
        if !self.flushed{
            let _ = flush(self);
        }
    }
}

fn flush(database: &Database) -> std::io::Result<()>{
    let mut contents = String::new();
    for (key, value) in &database.map {
        contents.push_str(key);
        contents.push('\t');
        contents.push_str(&value);
        contents.push('\n');
    }
    std::fs::write("kv.db", contents)
}
