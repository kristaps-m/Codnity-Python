import React from 'react';

function getDomain(urlIn) {
  let domain = (new URL(urlIn));
  return domain.hostname.replace('www.','');
}

const DataTable = ({ posts, loading }) => {
  if (loading) {
    return <h2>Loading...</h2>;
  }

  return (
    <div>
        <h3>This is HackerData page!</h3>
        <table className='table table-striped'>
          <thead>
            <tr>
              {/* <th>
                the_id
              </th> */}
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
            {posts.map(item =>
              <tr key={item.the_id}>
                {/* <td>{item.the_id}</td> */}
                <td>{item.title}</td>
                <td>
                  <a href={item.link} target="_blank" rel="noreferrer">                      
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
  );
};

export default DataTable;