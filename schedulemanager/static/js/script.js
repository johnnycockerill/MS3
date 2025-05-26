document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialisation
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // datepicker initialisation
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd mmmm, yyyy",
      i18n: {done: "Select"}
    });
    
    // select initialisation
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    // collapsibles initialisation
    let collapsible = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsible);
  });

   const coll = document.getElementsByClassName('collapsible');
   let i;

   for (i = 0; i < coll.length; i++) {
       coll[i].addEventListener('click', function() {
           this.classList.toggle('active');
           var content = this.nextElementSibling;

           if (content.style.display === 'block' || content.style.display === 'flex') {
               content.style.display = 'none';
           } else {
               content.style.display = 'block';
           }
       });
   }