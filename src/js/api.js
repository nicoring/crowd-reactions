import fetch from 'isomorphic-fetch'

// const API_URL = 'http://localhost:5000'
const API_URL = 'https://crowd-reactions-api.herokuapp.com:5000'

// Similar to:
// http://stackoverflow.com/questions/29473426/fetch-reject-promise-with-json-error-object
function fetchJson(url, request) {
  const finalRequest = request
    ? {
      ...request,
      body: JSON.stringify(request.body),
      headers: {
        ...request.headers,
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
    }
    : {
      method: 'GET',
      headers: {
        Accept: 'application/json',
      },
    }

  return fetch(url, finalRequest).then(
    (response) => {
      if (response.status >= 200 && response.status < 300) {
        return response.json()
      }
      // Reject other status
      return response.json().then(Promise.reject.bind(Promise))
    },
    error => Promise.reject(error) // Network or connection failure
  )
}

export function fetchInformation(query) {
  return fetchJson(`${API_URL}/ads/subway.json`)
}

export function postExample(userID, password) {
  return fetchJson(`${API_URL}/login`, {
    method: 'POST',
    body: {
      userID,
      password,
    },
  })
}


export function demoApi(){
  return new Promise( (resolve, reject) => {

  });
}
