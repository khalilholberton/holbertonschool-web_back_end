import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let usr;
  let image;

  try {
    usr = await createUser();
    image = await uploadPhoto();
  } catch (error) {
    photoval = null;
    userval = null;
  }
  return { photo: image, user: usr };
}
