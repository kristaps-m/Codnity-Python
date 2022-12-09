using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Data;
using System.Data.SqlClient;

namespace ycombinator.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class HackerdataController : ControllerBase
    {
        private readonly IConfiguration _configuration;

        public HackerdataController(IConfiguration configuration)
        {
            _configuration=configuration;
        }

        [HttpGet]
        public JsonResult Get()
        {
            string query = @"select * from dbo.scraped_data";

            DataTable table = new DataTable();
            string sqlDataSource = _configuration.GetConnectionString("HackerData");
            SqlDataReader myReader;
            using (SqlConnection myCon = new SqlConnection(sqlDataSource))
            {
                myCon.Open();
                using(SqlCommand myCommand = new SqlCommand(query, myCon))
                {
                    myReader = myCommand.ExecuteReader();
                    table.Load(myReader);
                    myReader.Close();
                    myCon.Close();
                }
            }

            return new JsonResult(table);
        }
    }
}
