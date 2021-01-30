import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const user_v = await createUser();
    const photo_v = await uploadPhoto();

  } catch (error) {
    return {
      photo: null,
      user: null,
    }
    return Promise.resolve({ photo_v, user_v });
}
