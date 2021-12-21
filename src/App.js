import './App.css';
import { useState, useEffect } from 'react';
import APIService from './APIService';
import { useCookies } from 'react-cookie'
import { useNavigate } from 'react-router-dom'

function App() {

  const [token, , removeToken] = useCookies(['Token'])
  const [sub, setSub] = useState('')
  const [isStudent, setIsStudent] = useState(false)
  const [isTeacher, setIsTeacher] = useState(false)
  const [data, setData] = useState({ 'id': '', 'data': {} })
  const [courses, setCourses] = useState([])
  const [query, setQuery] = useState({})
  const [formData, updateFormData] = useState({ 'courses': [], 'time': '' })
  const [slotData, setSlotData] = useState({})
  let already_teaching = []
  const [teaching, setTeaching] = useState([])
  let _ = []
  const [uName, setUName] = useState('')
  let navigate = useNavigate()

  const logoutbtn = () => {
    removeToken(['Token'])
  }

  useEffect(() => {
    if (!token['Token']) {
      navigate('/')
    }
  }, [token, navigate])

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/users', {
      'method': 'GET',
      'headers': {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token['Token']}`
      }
    })
      .then(resp => resp.json())
      .then(data => { setUName(data[0].username); setIsStudent(data[0].is_student); setIsTeacher(data[0].is_teacher) })
      .catch(err => console.log(err))
  }, [token])

  useEffect(() => {
    if (isTeacher) {
      fetch('http://127.0.0.1:8000/api/availabletiming/', {
        'method': 'GET',
        'headers': {
          'Content-Type': 'application/json',
          'Authorization': `Token ${token['Token']}`
        }
      })
        .then(resp => resp.json())
        .then(resp => { setData({ id: resp[0].id, data: resp[0].data }) })
        .catch(err => console.log(err))
      fetch('http://127.0.0.1:8000/api/addsubject/', {
        'method': 'GET',
        'headers': {
          'Content-Type': 'application/json',
          'Authorization': `Token ${token['Token']}`
        }
      })
        .then(resp => resp.json())
        .then(resp => {
          already_teaching = []
          Object.entries(resp).map(([key, value]) => {
            already_teaching.push(value.name);
          })
        })
        .then(() => { setTeaching(already_teaching) })
        .catch(err => console.log(err))
    }
    else {
      fetch('http://127.0.0.1:8000/get_subs', {
        'method': 'GET',
        'headers': {
          'Content-Type': 'application/json',
        }
      })
        .then(resp => resp.json())
        .then(resp => {
          _ = []
          Object.entries(resp).map(([key, value]) => {
            _.push(value.name)
          })
        })
        .then(() => { setCourses(_) })
    }
  }, [token, isTeacher, isStudent])

  const addsubbtn = () => {
    APIService.AddSubject({ name: sub }, token['Token'])
      .then(resp => { setTeaching([...teaching, resp.name]) })
      .catch(err => console.log(err))
  }

  const handlesubChange = (e) => {
    const target = e.target;
    let value = target.value;

    if (target.checked) {
      formData.courses.push(value);
      // console.log(formData)
    } else {
      formData.courses.splice(formData.courses.indexOf(value), 1);
      // console.log(formData)
    }
  };

  const handletimeChange = (e) => {
    formData.time = e.target.value;
    // console.log(formData)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    // console.log(formData);
    if (formData.courses.length === 0 || formData.time === '') {
      alert('Please fill all the fields')
      return;
    }
    fetch(`http://127.0.0.1:8000/get_query_results/?time=${formData.time}&courses=${formData.courses}`, {
      'method': 'GET',
      'headers': {
        'Content-Type': 'application/json',
      },
    })
      .then(resp => resp.json())
      .then(resp => JSON.parse(resp))
      .then(resp => { setQuery(resp) })
  };

  const slothandler = (e) => {
    let v = e.target.value;
    // console.log(v)
    let day = v.split('.')[0];
    let time = v.split('.')[1];
    // console.log(day, time)
    if (e.target.checked) {
      if (day in slotData) {
        slotData[day] += ', ' + time
      }
      else {
        slotData[day] = time;
      }
      console.log(slotData)
    }
    else {
      if (!(slotData[day].includes(','))) {
        delete slotData[day];
      }
      else {
        let r1 = ', ' + time
        let r2 = time + ', '
        slotData[day] = slotData[day].replace(r1, '').replace(r2, '').replace(time, '')
      }
      console.log(slotData)
    }
  }

  const updateslothandler = (e) => {
    fetch(`http://127.0.0.1:8000/api/availabletiming/${data.id}/`, {
      'method': 'PUT',
      'headers': {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token['Token']}`
      },
      body: JSON.stringify({ data: slotData })
    })
      .then(resp => resp.json())
      .then(resp => { setData({ id: resp.id, data: resp.data }) })
      .catch(err => console.log(err))
  }

  useEffect(
    () => {
      if (isStudent) { console.log(`fetchedData: ${query}`) }
    },
    [query, isStudent]
  )

  let days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
  let slots = ['8-9', '9-10', '10-11', '11-12', '12-1', '1-2', '2-3']

  return (
    <div className="App">

      <div className="row">
        <div className="col">

          <h2>Welcome {uName}</h2>
          <br />
        </div>

        <div className="col">
          <button onClick={logoutbtn} className="btn btn-primary">LOGOUT</button>
        </div>

        {isTeacher ?
          <div>
            <div className="mb-3">
              <label htmlFor="subject" className="form-label">Add a subject to the list of subjects you teach</label>
              <div className="row">
                <div className="col">
                  <input type="text" className="form-control" id="sub" placeholder="Please Enter a subject" value={sub} onChange={e => setSub(e.target.value)} />
                </div>
                <br />
                <div className="col">
                  <button onClick={addsubbtn} className="btn btn-primary" disabled={!sub}>Add</button>
                </div>
              </div>

            </div>
            <u><h5>Currently Teaching:</h5></u>
            {teaching.map((item, index) => { return <h6 key={index}>{item}</h6> })}
            <hr />
            <div className="mb-3">
              <u><h5>Current Availabilities</h5></u>
              {
                Object.entries(data.data).map(([key, value]) => <h6 key={key}>{key} : {value}</h6>)
              }
            </div>
            <br />
            <u><i>(Select the <b>days</b> and the <b>coressponding timeslots</b> for which you are available.)</i></u>
            {days.map(day => {
              return <div className="row">
                <div className="col">
                  <p>{day} : </p>
                </div>
                {slots.map(slot => {
                  return <div className="col">
                    <input type="checkbox" value={`${day}.${slot}`} onChange={slothandler} />&nbsp;{slot}
                  </div>
                })}
              </div>
            })}
            <button onClick={updateslothandler} className="btn btn-primary">Update</button>
            <hr />
          </div>
          :
          <div>

            <div className="mb-3">
              <h3><label htmlFor="course" className="form-label"><u>Courses Available</u></label></h3>
              {courses.length > 0 ?
                <div className="row">
                  {courses.map((course, _) => <div className="col"><input onChange={handlesubChange} key={_} type="checkbox" value={course} />{course}</div>)}
                </div>
                : <h5>Sorry, no courses available</h5>
              }
              <br />
              <label htmlFor="time" className="form-label">Select your preferred Time&nbsp;&nbsp;&nbsp;&nbsp;</label>
              <select onChange={handletimeChange} defaultValue={'DEFAULT'}>
                <option value="DEFAULT" disabled>Select</option>
                {slots.map(slot => <option key={slot} value={slot}>{slot}</option>)}
              </select>
              <br></br>
              <button onClick={handleSubmit} className="btn btn-success">Search</button>
              <br /><br />

              {Object.keys(query).length > 0 ?
                <div>
                  <i><h6>Format of Result: <br />(subject_name)&nbsp; : &nbsp;(list of all available teacherst)&nbsp; : &nbsp;(list of all days the teacher is available for the queried time slot)</h6></i>
                  {JSON.stringify(query, null, 10)}
                </div>
                : null}

            </div>

          </div>

        }

      </div>

    </div>
  );
}

export default App;