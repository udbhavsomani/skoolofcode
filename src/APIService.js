export default class APIService {

    static AddSubject(body, token) {
        return fetch('https://skoolofcode-api.herokuapp.com/api/addsubject/', {
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
            },
            body: JSON.stringify(body)
        }).then(resp => resp.json())
    }

    static LoginUser(body) {
        return fetch('https://skoolofcode-api.herokuapp.com/auth/', {
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body)
        }).then(resp => resp.json())
    }

    static RegisterUser(body) {
        return fetch('https://skoolofcode-api.herokuapp.com/api/users/', {
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body)
        }).then(resp => resp.json())
    }
}