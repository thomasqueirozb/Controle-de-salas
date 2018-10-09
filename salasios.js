function makeHttpObject() {
  try {
    return new XMLHttpRequest();
  } catch (error) {}
  try {
    return new ActiveXObject("Msxml2.XMLHTTP");
  } catch (error) {}
  try {
    return new ActiveXObject("Microsoft.XMLHTTP");
  } catch (error) {}

  throw new Error("Could not create HTTP request object.");
}

function get_all(sala) {

  var request = makeHttpObject();
  request.open("GET", "", true);
  request.send(null);
  request.onreadystatechange = () => {
    if (request.readyState == 4) {
      return sort(sala, request);
    }
  }
};

function sort(sala,request) {
  sala = sala.split(' ');

  let semestre = sala[0];
  let curso = sala[1];
  let letra = sala[2];

  var l = []
  var res = request.responseXML;
  var events = res.getElementsByTagName('CalendarioEvento')
  for (let event of events) {
    let turma = event.getElementsByTagName('turma')[0].innerHTML
    if (turma) {
      if (
        (turma.substring(0, 1) == semestre) &&
        (turma.substring(3, 3 + curso.length) == curso) &&
        (turma.substring(4 + curso.length, 5 + curso.length) == letra)
      ) {

        let horainicio = event.getElementsByTagName('horainicio')[0].innerHTML;
        let horatermino = event.getElementsByTagName('horatermino')[0].innerHTML;
        let sala_curso = event.getElementsByTagName('sala')[0].innerHTML;
        let andar = event.getElementsByTagName('andar')[0].innerHTML;
        let titulo = event.getElementsByTagName('titulo')[0].innerHTML;

        l.push({
          titulo,
          horainicio,
          horatermino,
          sala_curso,
          andar
        })
      }
    }
  }
  console.log(l);
  // return l;
}
