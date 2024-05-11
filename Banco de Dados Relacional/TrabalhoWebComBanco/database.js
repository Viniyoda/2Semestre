const { createPool } = require ('mysql');

const pool = createPool({
    host: "mysql-joguinho-viniyoda360-d36d.f.aivencloud.com",
    user: "avnadmin",
    password: "AVNS_KPxvTUUtahG1o6-uTlV",
    database: "joguinhodb",
    connectionLimit: 10
})

pool.query("select * from  usuarios", (err, result, fields)=>{
    if(err){
        return console.log(err);
    }
    return console.log(result);
})