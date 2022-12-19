import React, { useState, useEffect } from 'react';
import './Post.css';

const BASE_URL = 'http://localhost:8000/';

function Post({ post }) {
  const [imageUrl, setImageUrl] = useState('');

  useEffect(() => {
    setImageUrl(BASE_URL + post.image_url);
  }, [post.image_url]);

  return (
    <div className="post">
      <img className="post_image" src={imageUrl} alt="post" />
    </div>
  );
}

export default Post;
