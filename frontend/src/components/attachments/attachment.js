import React from 'react';

const Attachment = (props) => {
    return (
        <div>
            <h6>{props.attachment_type}</h6>
            <p>{props.attachment_name}</p>
        </div>
    );
}

export default Attachment;