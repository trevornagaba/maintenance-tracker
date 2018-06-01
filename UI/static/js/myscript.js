function searchFunction() {
    var input = document.getElementById("search");

    /*Capitalize search term*/
    var filter = input.value.toUpperCase();

    var table = document.getElementById("myTable");

    /*Add all elements with tag name tr to array tr*/
    var tr = table.getElementsByTagName("tr");

    /*Cycle through elements in array tr*/
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            /*return first index at which search term can be found
            and therefore execute if statment if it exists*/
            if (td.innerHTML.toUpperCase().indexOf(filter) >= 0) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }          
    }
}