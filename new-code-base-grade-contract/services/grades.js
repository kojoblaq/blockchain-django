'use strict';
const blockchain = require('/home/project/blockchain-django/new-code-base-grade-contract/lib/new-grade-contract.js')
const b = new blockchain();
console.log(b);
// const fs = require('fs')
// const {FileSystemWallet, gateway} = require('fabric-network')
// const wallet = FileSystemWallet('./_wallet')
const path = require('path');
const sqlite = require('better-sqlite3');
const db = new sqlite(path.resolve('./nodejs-sqlite/grades.db'), { fileMustExist: true });
// const db = new sqlite(path.resolve('/home/project/blockchain-django/gradeStructure/db.sqlite3'), { fileMustExist: true });
const config = require('../config');

function getMultiple(page = 1) {
    const offset = (page - 1) * config.listPerPage;
    // const data = db.prepare('SELECT * FROM fairwages_grade LIMIT ?,?').all(offset, config.listPerPage);
    const data = db.prepare('SELECT * FROM grade LIMIT ?,?').all(offset, config.listPerPage);
    const meta = { page };

    return {
        data,
        meta
    };
}
// this is reading a single grade with a particular staaf id given
async function getUserGrade(id,page=1) {
    const offset = (page - 1) * config.listPerPage;
    // const data = db.prepare('SELECT * FROM fairwages_grade LIMIT ?,?').all(offset, config.listPerPage);
    const data = db.prepare('SELECT * FROM grade WHERE staff_id = ? LIMIT ?,?').all(id,offset, config.listPerPage);
    console.log(`Succesfully read grade of staff with staffID:${id}`);
    const meta = { page };
    return {
        data,
        meta
    };
}

function createGrade (staffId,ss_grade, inst_name, job_t, staffName,salary , creator, status){
    const data = db.prepare('INSERT INTO grade (staff_id,staff_grade,institution_name, job_role, staff_name, salary, creator, status) VALUES(?,?,?,?,?,?,?,?)')
        .run(staffId,ss_grade, inst_name, job_t, staffName, salary, creator, status);
    console.log(`Succesfully created for ${staffName} with ID:${staffId}`);
    const gateway = new Gateway();

    // try{
    //     const indentityLabel = 'org1peer-api.127-0-0-1.nip.io:8088';
    //     // load connection profile
    //     let ccpFile = fs.readFileSync('NewOrg1GatewayConnection.json');
    //     const ccp = JSON.parse(ccpFile.toString());


    //     // set connection options

    //     let connectionOptions = {
    //         identity: indentityLabel,
    //         wallet:wallet,
    //         discovery: {
    //             asLocalHost: true
    //         }
    //     };

    //     // connect to gateway using application specified parameters
    //      await gateway.connect(ccp, connectionOptions);
    //     console.log('connected to fabric gateway');

    //     //get accessibilty network (channel)
    //     const network = await gateway.getNetwork('mychannel');
    //     //
    //     const contraact = await network.getContract('NewGradeContract');

    //     //
    //     var response = await contraact.submitTransaction('create_Grade');
    //     console.log('Transaction Response:', response.toString());
    // } catch(error){
    //     console.log('Error processing transaction. ${error}');
    //     console.log(error.stack);


    // }finally{
    //     console.log("Disconnect from Network");
    //     gateway.disconnect();
    // }


  
    // const meta = { page };
    b.create_Grade(staffId,ss_grade, inst_name, job_t, staffName, status, creator, salary);
    // const data = {success:true};
    return {
       data
    };

}
function updateGrade (ss_grade,inst_name, job_t, staffName,salary,creator,status,staffId ){
    const data = db.prepare('UPDATE grade SET staff_grade=?,institution_name=?, job_role=?, staff_name=?, salary=?, creator=?, status=? WHERE staff_id = ?')
                    .run(ss_grade, inst_name, job_t, staffName, salary, creator, status,staffId );
    console.log(`Successfully updated the grade of staff with ID:${staffId}`);
    // const meta = { page };
    b.update_Grade(ss_grade, inst_name, job_t, staffName, status, salary);
    return {
        data
    };

}
function deleteGrade (staffId ){
    const data = db.prepare('DELETE FROM grade WHERE staff_id = ?')
                    .run(staffId );
    console.log(`Successfully Deleted grade of staff with ID:${staffId}`);
    // const meta = { page };
    b.deleteNewGrade(staffId);
    return {
        data        
    };

}





module.exports = {
    getMultiple,
    getUserGrade,
    deleteGrade,
    updateGrade,
    createGrade
};
