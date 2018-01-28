import React, { Component } from 'react';

import { Navbar, Nav, NavItem, Glyphicon, NavDropdown, MenuItem } from 'react-bootstrap';

class OtherBar extends React.Component{

  constructor(props) {
    super(props);
  }


  render(){
	   return <Navbar fluid collapseOnSelect className="otherBar">
		    <Navbar.Header>
		      <Navbar.Brand>
		        <a href="/">Makan Jio&nbsp;<Glyphicon glyph="ice-lolly-tasted" /></a>
		      </Navbar.Brand>
		      <Navbar.Toggle />
		    </Navbar.Header>
		    	<Navbar.Collapse>
			    	<Nav pullRight>
				        <MenuItem>Help&nbsp;<Glyphicon glyph="info-sign" /></MenuItem>
	            		<MenuItem>Logout&nbsp;<Glyphicon glyph="log-out" /></MenuItem>
			        </Nav>
			    </Navbar.Collapse>
		  </Navbar>;	
  }
};


export default OtherBar
