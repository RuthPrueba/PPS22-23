export function validaNombre(nombre) {
  if (nombre.length < 1) return "Este campo es obligatorio";
  else return true;
}

export function validaEmail(email) {
  if (email.length < 1) return "Este campo es obligatorio";
  else if (
    email.match(
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    )
  )
    return true;
  else return "Introduce un email válido";
}

export function validaCV(cv) {
    if (cv.size < 1) return "Este campo es obligatorio";
    else return true;
  }