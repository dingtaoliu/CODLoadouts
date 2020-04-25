import React, { useEffect, useState } from 'react';
import Attachment from "../attachments/attachment";

const TestDash = () => {
    const [attachment, setAttachment] = useState({});

    useEffect(() => {
        const fetch_attachment = async() => { 
            const response = await fetch('/api/attachments/');
            const data = await response.json();
            setAttachment(data[0])
            
        };
        fetch_attachment();
    }, []);

    return (
        <div>
            <Attachment {...attachment}/>
        </div>
    );
}

export default TestDash;