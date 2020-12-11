import React from 'react';
import Modal from 'react-bootstrap/Modal';

const ModalComponent = ({ participant, show, setShow }) => {
  return (
    <Modal size='sm' show={show} onHide={() => setShow(false)}>
      <Modal.Dialog>
        <Modal.Header closeButton>
          <Modal.Title>{participant.name}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>Ikä: 33 {participant.age}</p>
          <p>Aika: {participant.result}</p>
          <p>Matkan pituus: {participant.distance}</p>
        </Modal.Body>
      </Modal.Dialog>
    </Modal>
  );
};

export default ModalComponent;
