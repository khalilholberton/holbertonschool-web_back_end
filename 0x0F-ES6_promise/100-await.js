import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let user_v;
  let photo_v;

  try {
    user_v = await createUser();
    photo_v = await uploadPhoto();

    return Promise.resolve({ photo_v, user_v });
  } catch (err) {
    return {
      photo: null,
      user: null,
    };
