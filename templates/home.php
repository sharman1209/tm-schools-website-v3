<!DOCTYPE php>
<html>
  <head>
    <title>TM Schools Dashboard</title>
    <meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  </head>
  <body>
    {% include 'nav.html' %}
    {% include 'banner.html' %}
    <div class="container">
    <h1 class="text-center mt-2 mb-4"> TM Schools Search
    </h1>
    <p class="lead">
      This interactive searching tool allows users to explore information about different schools in Malaysia effortlessly. Users can search for schools by entering the School Code or School Name, and the application provides details such as the School Code, School Name, TM Interim Status, and TM Hybrid Status.
    </p>
      
      <label class="mt-2 mb-2" for="exampleAddress" class="">Enter School Code Here :</label>
      
      <div class="mb-2">

        <form action="" method="GET">
            <input type="text" name="search" value="<?php if(isset($_GET['search'])){echo $_GET['search']; } ?>" class="form-control" placeholder="Search">
            <div class="mt-2">
                <button type="submit" class="btn btn-primary">Search</button>
                <button type="reset" class="btn btn-danger">Reset</button>
            </div>
        </form>

      </div>
      
      <div class="col-md-12">
          <div class="card">
              <div class="card-header"
                  <h4 class="text-center">Search Results</h4>
              </div>
              <div class="card-body">

                <table class="table table-bordered">
                  <thread>
                    <tr>
                      <th>KOD SEKOLAH</th>
                      <th>SENARAI SEKOLAH MALAYSIA</th>
                      <th>SEKOLAH INTERIM</th>    
                      <th>SEKOLAH VSAT</th> 
                      <th>SEKOLAH HYBRID</th> 
                    </tr>
                  <thread>
                  <tbody>

                    <?php

                    if(isset($_REQUEST['search']))
                    {

                        $connection = mysqli_connect("aws.connect.psdb.cloud", "oegmu7fkapga3wwu6aet", "pscale_pw_aGt8OFVbcuIbODwDq34i50F9X7cxmBOFuWHSDZ1Vkk2", "tm_schools");
                        $filtervalue = $_GET['search'];
                        $filterdata = "SELECT * FROM tm_schools WHERE CONCAT(KOD SEKOLAH, SENARAI SEKOLAH MALAYSIA, SEKOLAH INTERIM, SEKOLAH VSAT, SEKOLAH HYBRID) LIKE '%$filtervalue%'"
                        $filterdata_run = mysqli_query($connection, $filterdata);

                        if(mysqli_num_rows($filterdata_run) > 0)
                        {
                          foreach($filterdata_run as $row)
                            {
                              ?>
                                <tr>
                                  <td><?php echo $row['KOD SEKOLAH']; ?></td>
                                  <td><?php echo $row['SENARAI SEKOLAH MALAYSIA']; ?></td>
                                  <td><?php echo $row['SEKOLAH INTERIM']; ?></td>
                                  <td><?php echo $row['SEKOLAH VSAT']; ?></td> 
                                  <td><?php echo $row['SEKOLAH HYBRID']; ?></td> 
                                </tr>
                              <?php
                            }
                        }
                        else
                        {
                          ?>
                    <tr>
                      <td colspan="4">No record found</td>
                    </tr>
                          <?php
                        }
                    }
        </div>
    
    </div>
    
    {% include "footer.html" %}
  </body>
</html>