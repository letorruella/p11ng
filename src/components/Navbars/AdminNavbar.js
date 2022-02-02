/*!

=========================================================
* Black Dashboard React v1.2.0
=========================================================

* Product Page: https://www.creative-tim.com/product/black-dashboard-react
* Copyright 2020 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/black-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
// nodejs library that concatenates classes
import classNames from "classnames";

// reactstrap components
import {
  
  Navbar,
 
} from "reactstrap";

function AdminNavbar(props) {
  
  // function that adds color white/transparent to the navbar on resize (this is for the collapse)
  
  return (
    <>
      <Navbar className={classNames("navbar bg-white")} expand="">
        # hello
      </Navbar> 
    </>
  );
}

export default AdminNavbar;
