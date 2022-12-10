import React, {Component} from 'react';
import {variables} from './Variables.js'

function getDomain(urlIn) {
  let domain = (new URL(urlIn));
  return domain.hostname.replace('www.','');
}

export class HackerData extends Component {

  constructor (props) {
    super(props);

    this.state ={
      hackerdataList:[]
    }
  }

  refreshList(){
    fetch(variables.API_URL+'Hackerdata')
    .then(response => response.json())
    .then(data => this.setState({hackerdataList:data}))
  }

  componentDidMount(){
    this.refreshList();
  }

  render (){
    const {hackerdataList} = this.state;
    return (
      <div>
        <h3>This is HackerData page!</h3>
        <table className='table table-striped'>
          <thead>
            <tr>
              <th>
                the_id
              </th>
              <th>
                title
              </th>
              <th>
                link
              </th>
              <th>
                points
              </th>
              <th>
                date_created
              </th>
            </tr>
          </thead>
          <tbody>
            {hackerdataList.map(item =>
              <tr key={item.the_id}>
                <td>{item.the_id}</td>
                <td>{item.title}</td>
                <td>
                  <a href={item.link}>                      
                    {getDomain(item.link)}                      
                  </a>
                </td>
                <td>{item.points}</td>
                <td>{item.date_created}</td>                
              </tr>
              )}
          </tbody>
        </table>
      </div>
    )
  }
};