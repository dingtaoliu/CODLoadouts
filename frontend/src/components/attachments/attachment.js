import React from 'react';
import ListGroup from 'react-bootstrap/ListGroup'

const Attachment = (props) => {
    return (
      <ListGroup horizontal='sm'>
        <ListGroup.Item>{props.attachment_type}</ListGroup.Item>
        <ListGroup.Item>{props.attachment_name}</ListGroup.Item>
      </ListGroup>
    );
}

export default Attachment;