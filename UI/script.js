let submitValue = function () {
  let eventID = parseInt(document.getElementById("eventID").value);
  let species = document.getElementById("species").value;
  let altitude = parseInt(document.getElementById("altitude").value);
  let distance = parseInt(document.getElementById("distance").value);
  let tensed = parseInt(document.getElementById("tensed").value);

  var JSONobj = {"altitudeMoved":altitude, "distanceMoved":distance, "tensed":tensed};
  console.log(JSONobj)
  let xhr = new XMLHttpRequest();

  // input from api
  let result = 1;
  document.getElementById("contact").submit()
  // 2. Configure it: GET-request for the URL /article/.../load
  /*xhr.open('POST', 'http://9.199.146.17:2345/predict');
  
  xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');
  // 3. Send the request over the network
  xhr.send(JSONobj);*/

  // 4. This will be called after the response is received
  /*
  xhr.onreadystatechange = function() {
    if (xhr.status != 200) { // analyze HTTP status of the response
      alert(`Error ${xhr.status}: ${xhr.statusText}`); // e.g. 404: Not Found
        }
    else
     { // show the result
      result = xhr.response.prediction;
      console.log(result);
      if (result == "[0]") {
      document.getElementById("result").innerHTML = "The disaster is NOT likely to happen" ;
          }
      else {
        document.getElementById("result").innerHTML = "The disaster is MORE likely to happen, Please Stay Safe" ;
      }
}
    }
    */
  };
