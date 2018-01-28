import React from 'react'
import {Col, Button, FormGroup, ControlLabel, FormControl, Form, Glyphicon} from 'react-bootstrap'
import GoogleMapReact from 'google-map-react';

import { connect } from 'react-redux'

import {Link} from 'react-router-dom'
import OtherBar from '../common/otherbar'

class FeedbackForm extends React.Component{
  
  constructor(props) {
  	super(props);

    this.state = {
      title: "",
      description: "",
      hide: true,
      clicks: 5
    }

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.mapClick = this.mapClick.bind(this);
  }

  mapClick() {
      console.log("HIHI");
      var clicks = this.state.clicks;
      clicks--;
      this.setState({clicks: clicks})
      console.log(this.state.clicks);
      if (this.state.clicks < 0) {
        this.setState({hide: false});
      } else {
        this.setState({hide: true});
      }
  }

  handleChange(event) {
    const name = event.target.name;
    const value = event.target.value;

    this.setState({
      [name]: value,
    });
  }

  handleSubmit(event) {
      event.preventDefault();
      
      if (this.state.post === '' || this.state.header === '' || this.state.topic === '') {
         alert('Fields cannot be blank!');
      } else {
         
      }
  }

  render(){

    const centre = {lat: 1.37, lng: 103.83};
    const Marker = (props) => {return <h1 className="glyphicon glyphicon-cutlery"></h1> };

    return(
        <div>
          <OtherBar/>
    	  <div className="container">
          <h3>Create an Event</h3>
          <p>Fill up the details below to get started</p>
          <hr/>
          <Form horizontal onSubmit={this.handleSubmit}>

            <FormGroup controlId="formHorizontalHeader">
              <Col componentClass={ControlLabel} sm={2}>
                Title
              </Col>
              <Col sm={10}>
                <FormControl 
                  type="text" placeholder="Write an appropriate header for your post here" 
                  name="header" value={this.state.header}
                  onChange={this.handleChange}
                />
              </Col>
            </FormGroup>

            <FormGroup controlId="formHorizontalPost">
              <Col componentClass={ControlLabel} sm={2}>
                Description
              </Col>
              <Col sm={10}>
                <FormControl 
                  componentClass="textarea" placeholder="Write your post! Drag out the box if you need more room" 
                  name="post" value={this.state.post}
                  onChange={this.handleChange}
                />
              </Col>
            </FormGroup>

            <div id="createMap" onClick={this.mapClick}>
              <GoogleMapReact
                defaultCenter={centre}
                defaultZoom={13}
              >
               {!this.state.hide && <Marker
                  lat={1.4034}
                  lng={103.9055}
                />}
              </GoogleMapReact>
            </div>

            <br/>
            <hr/>

            <FormGroup>
              <Col smOffset={2} sm={10}>
                <Button type="submit">
                  Create
                </Button>
              </Col>
            </FormGroup>
          </Form>
        </div>
        </div>
    );
  }
};

export default FeedbackForm;
  
