export default class APIService {

    static AddSubject(body, token) {
        return fetch('http://127.0.0.1:8000/api/addsubject/', {
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
            },
            body: JSON.stringify(body)
        }).then(resp => resp.json())
    }

    static LoginUser(body) {
        return fetch('http://127.0.0.1:8000/auth/', {
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body)
        }).then(resp => resp.json())
    }

    static RegisterUser(body) {
        return fetch('http://127.0.0.1:8000/api/users/', {
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body)
        }).then(resp => resp.json())
    }
}