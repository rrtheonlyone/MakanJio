import React, { Component } from 'react';

import { Navbar, Nav, NavItem, Glyphicon, NavDropdown, MenuItem } from 'react-bootstrap';

class NavBar extends React.Component{

  constructor(props) {
    super(props);
  }

  render(){
	return <Navbar fluid collapseOnSelect id="loginbar">
		    <Navbar.Header>
		      <Navbar.Brand>
		        <a href="/">Makan Jio&nbsp;<Glyphicon glyph="ice-lolly-tasted" /></a>
		      </Navbar.Brand>
		      <Navbar.Toggle />
		    </Navbar.Header>
		  </Navbar>;	
  }
};


export default NavBar
