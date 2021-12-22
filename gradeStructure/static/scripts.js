const readGrades = () => {
    axios.get('http://localhost:3000/get-grades')
        .then(response => {
            const grades = response.data.data;
            console.log(`GET grades`, grades);
        })
        .catch(error => console.error(error));
};

readGrades();