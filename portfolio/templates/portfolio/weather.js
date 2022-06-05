

var weatherData = document.getElementById("weather_data");
  weatherData.addEventListener('click',function(e){
 e.preventDefault();
 var cityName = document.getElementById("cityName").value;
 var url = "https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid=38440d6588cb8e97791a0a6db25b1f5c";
  if(cityName == ""){
      alert("Enter a city name");
  }else{
  fetch(url).then(function(response){
      if(response.ok){
          return response.json();
      }else{
          throw new Error(Error);
      }
  }).then(function(data){
    const html =    `
        <h2 class="text-danger text-center"><span class="text-dark">City:</span>${data.name}</h2>
        ` ;
      document.getElementById("display_data").innerHTML = html;
  }).catch(function(error){
      console.log(error);
  });
  }
});