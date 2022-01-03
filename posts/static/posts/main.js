const box = document.getElementById('hello-world');

$.ajax({
    type:'GET',
    url:'/hello-world/',
    success:function(response){
        console.log('success',response)
        box.textContent = response.text
    },
    error:function(error){
        console.log('error',error)
    }
})