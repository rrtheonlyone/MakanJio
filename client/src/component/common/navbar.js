import React, { Component } from 'react';

import { Navbar, Nav, NavItem, Glyphicon, NavDropdown, MenuItem } from 'react-bootstrap';

class NavBar extends React.Component{

  constructor(props) {
    super(props);

    this.state = {
    	hover: false
    }
  }

  componentDidMount() {
    document.addEventListener('scroll', () => {
      if (window.scrollY > 10) {
      	this.setState({hover: true});
      } else {
      	this.setState({hover: false});
      }
  	})
  }

  render(){

  	const navClass = (this.state.hover) ? "purpleNav" : "transparentNav";

	return <Navbar fluid collapseOnSelect fixedTop className={navClass}>
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


export default NavBar
