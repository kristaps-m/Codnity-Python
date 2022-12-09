import logo from './logo.svg';
import './App.css';
import {Home} from './Home';
import { HackerData } from './HackerData';
import { BrowserRouter, Route, Routes, NavLink } from 'react-router-dom'; 
//  Switch

function App() {
  return (
    <BrowserRouter>
    <div className="App">
      <h3 className = "d-flex justify-content-center m-3">
        React JS FrontEnd
      </h3>
      <nav className='navbar navbar-expand-sm bg-light navbar-dark'>
        <ul className='navbar-nav'>
          <li className='nav-item- m-1'>
            <NavLink className="btn btn-light btn-outline-primary" to="/home">
              Home
            </NavLink>
          </li>
          <li className='nav-item- m-1'>
            <NavLink className="btn btn-light btn-outline-primary" to="/hackerdata">
              HackerData
            </NavLink>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path='/home' element={<Home/>}/>
        <Route path='/hackerdata' element={<HackerData/>}/>
      </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;
