var city = $("#city").text();

const settings = {
	"async": true,
	"crossDomain": true,
	"url": `https://community-open-weather-map.p.rapidapi.com/weather?q=${city}&units=imperial`,
	"method": "GET",
	"headers": {
		"x-rapidapi-key": "d7cb94f27dmsh96d3dabd8b73ea8p1e8114jsn6514282cc8de",
		"x-rapidapi-host": "community-open-weather-map.p.rapidapi.com"
	}
};

$.ajax(settings).done(function (response) {
	console.log(response);
	var weather = response.weather[0];
	$("#temperature").append(response.main.temp).append("˚");
	$("#feels_like").append(response.main.feels_like).append("˚");
	$("#temp_min").append(response.main.temp_min).append("˚");
	$("#temp_max").append(response.main.temp_max).append("˚");
	$("#weather").append(`${weather.main} - ${weather.description}`);
});