import React from 'react';
import ListGroup from 'react-bootstrap/ListGroup'
import Media from 'react-bootstrap/Media'
import "./attachment.css"

const Attachment = (props) => {
    return (
      <Media>
        <ListGroup className="col-sm-2">
          <ListGroup.Item className="attachmentType">{props.attachment_type}</ListGroup.Item>
          <ListGroup.Item className="attachmentName">{props.attachment_name}</ListGroup.Item>
        </ListGroup>
        <img
          height={100}
          src={require("../../imgs/placeholder.jpg")}
        />
      </Media>
    );
}

export default Attachment;