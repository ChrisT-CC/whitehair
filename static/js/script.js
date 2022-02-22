document.addEventListener('DOMContentLoaded', function() {
    
    // initialize sidenav
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // initialize select
    select = document.querySelectorAll('select');
    M.FormSelect.init(select);

    // initialize collapsible
    collapse = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapse);

});