"""Testing measurement"""
# Copyright 2019 HQS Quantum Simulations GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest
import numpy.testing as npt
from pyquest_cffi import cheat
from pyquest_cffi import utils
import numpy as np


def test_calc_simple() -> None:
    """Testing simple calc functions.
    
    calcPurity, calcFidelity, calcInnerProduct, calcProbofOutcome, calcTotalProb
    """
    env = utils.createQuestEnv()()
    qureg = utils.createQureg()(2, env)
    qureg_main = utils.createQureg()(2, env)
    cheat.initZeroState()(qureg)

    with npt.assert_warns(RuntimeWarning):
        purity = cheat.calcPurity()(qureg)
        density_inner_product = cheat.calcDensityInnerProduct()(qureg1=qureg,
                                                                            qureg2=qureg_main)
    fidelity = cheat.calcFidelity()(qureg=qureg_main,
                                                qureg_reference=qureg)
    inner_product = cheat.calcInnerProduct()(qureg1=qureg,
                                                         qureg2=qureg_main)
    prob_of_outcome = cheat.calcProbOfOutcome()(qureg, 1, 0)
    total_prob = cheat.calcTotalProb()(qureg)

    assert purity is None
    assert fidelity == 1
    assert (inner_product.real == 1 and inner_product.imag == 0)
    assert prob_of_outcome == 1.0
    assert total_prob == 1
    assert density_inner_product is None

    qureg = utils.createDensityQureg()(2, env)
    cheat.initZeroState()(qureg)

    with npt.assert_warns(RuntimeWarning):
        fidelity = cheat.calcFidelity()(qureg=qureg_main,
                                                    qureg_reference=qureg)
        inner_product_1 = cheat.calcInnerProduct()(qureg1=qureg,
                                                               qureg2=qureg_main)
        inner_product_2 = cheat.calcInnerProduct()(qureg1=qureg_main,
                                                               qureg2=qureg)
        inner_product_3 = cheat.calcInnerProduct()(qureg1=qureg,
                                                               qureg2=qureg)
        density_inner_product_1 = cheat.calcDensityInnerProduct()(qureg1=qureg,
                                                                            qureg2=qureg_main)
        density_inner_product_2 = cheat.calcDensityInnerProduct()(qureg1=qureg_main,
                                                                            qureg2=qureg)
    density_inner_product_3 = cheat.calcDensityInnerProduct()(qureg1=qureg,
                                                                        qureg2=qureg)
    purity = cheat.calcPurity()(qureg)
    prob_of_outcome = cheat.calcProbOfOutcome()(qureg, 1, 0)
    total_prob = cheat.calcTotalProb()(qureg)

    assert purity == 1
    assert fidelity is None
    for inner_product in [inner_product_1, inner_product_2, inner_product_3]:
        assert inner_product is None
    assert prob_of_outcome == 1.0
    assert total_prob == 1
    assert [density_inner_product_1, density_inner_product_2] == [None, None]
    assert density_inner_product_3 == 1


def test_get_simple() -> None:
    """Testing simple get functions.

    getStateVectoratIndex/getAmp, getDensityMatrixatRowColumn/getDensityAmp,
    getAbsoluteValSquaredatIndex/getProbAmp, getRealAmp, getImagAmp
    """
    env = utils.createQuestEnv()()
    qureg = utils.createQureg()(2, env)
    cheat.initZeroState()(qureg)
    index = 1
    operator_matrix = np.array([[1, 0, 2, 0], [0, 1, 0, 2], [0, 2, 0, 1], [2, 0, 1, 0]])

    with npt.assert_warns(RuntimeWarning):
        density_matrix = cheat.getDensityAmp()(qureg=qureg, row=1, column=1)
    state_vec = cheat.getAmp()(qureg=qureg, index=index)
    abs_val_state_vec = cheat.getProbAmp()(qureg=qureg, index=1)
    real_val_sate_vec = cheat.getRealAmp()(qureg=qureg, index=1)
    imag_val_sate_vec = cheat.getImagAmp()(qureg=qureg, index=1)
    num_amps = cheat.getNumAmps()(qureg=qureg)
    num_qubits = cheat.getNumQubits()(qureg=qureg)
    expec_val = cheat.getExpectationValue()(qureg=qureg,
                                            operator_matrix=operator_matrix)

    assert state_vec == 0
    assert density_matrix is None
    assert abs_val_state_vec == 0
    assert real_val_sate_vec == 0
    assert imag_val_sate_vec == 0
    assert num_amps == 4
    assert num_qubits == 2
    assert expec_val == 1

    qureg = utils.createDensityQureg()(2, env)
    cheat.initZeroState()(qureg)

    with npt.assert_warns(RuntimeWarning):
        state_vec = cheat.getAmp()(qureg=qureg, index=index)
        abs_val_state_vec = cheat.getProbAmp()(qureg=qureg, index=1)
        real_val_sate_vec = cheat.getRealAmp()(qureg=qureg, index=1)
        imag_val_sate_vec = cheat.getImagAmp()(qureg=qureg, index=1)
    density_matrix = cheat.getDensityAmp()(qureg=qureg, row=1, column=1)
    # num_amps = cheat.getNumAmps()(qureg=qureg)
    num_qubits = cheat.getNumQubits()(qureg=qureg)
    expec_val = cheat.getExpectationValue()(qureg=qureg,
                                            operator_matrix=operator_matrix)

    assert state_vec is None
    assert density_matrix == 0
    assert abs_val_state_vec is None
    assert real_val_sate_vec is None
    assert imag_val_sate_vec is None
    # assert num_amps == 4
    assert num_qubits == 2
    assert expec_val == 1


def test_get_complicated() -> None:
    """Test less simple get functions

    getDensityMatrix,
    """
    env = utils.createQuestEnv()()
    qureg_statevec = utils.createQureg()(2, env)
    qureg_dens = utils.createDensityQureg()(2, env)
    cheat.initZeroState()(qureg_statevec)
    cheat.initZeroState()(qureg_dens)

    dens_mat = cheat.getDensityMatrix()(qureg=qureg_dens)
    state_vec = cheat.getStateVector()(qureg=qureg_statevec)

    occupation_proba_dens = cheat.getOccupationProbability()(qureg=qureg_dens)
    occupation_proba_statevec = cheat.getOccupationProbability()(qureg=qureg_statevec)

    repeated_meas_dens = cheat.getRepeatedMeasurement()(qureg=qureg_dens,
                                                        number_measurements=5,
                                                        qubits_to_readout_index_dict={0: 0, 1: 1})
    repeated_meas_statevec = cheat.getRepeatedMeasurement()(qureg=qureg_statevec,
                                                            number_measurements=5,
                                                            qubits_to_readout_index_dict={0: 0, 1: 1})

    assert np.all(dens_mat == np.array([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
    assert np.all(state_vec == np.array([1, 0, 0, 0]))
    assert np.all(occupation_proba_dens == np.array([1, 0, 0, 0]))
    assert np.all(occupation_proba_statevec == np.array([1, 0, 0, 0]))
    assert np.all(repeated_meas_dens == np.array([[0., 0.]] * 5))
    assert np.all(repeated_meas_statevec == np.array([[0., 0.]] * 5))


def test_calc_Expec_Pauli_Sum() -> None:
    """Test calculating the expectation value of a pauli sum"""
    env = utils.createQuestEnv()()
    qubits = utils.createQureg()(4, env)
    workspace = utils.createQureg()(4, env)
    a = cheat.calcExpecPauliSum()(
        qureg=qubits,
        paulis=[[0, 1, 2, 3], [3, 2, 1, 0]],
        coefficients=[0.4, 0.3],
        workspace=workspace,
    )
    assert a == 0.0


def test_calc_Hilbert_Schmidt_distance() -> None:
    """Test calculating the Hilbert Schmidt distance"""
    env = utils.createQuestEnv()()
    qureg1 = utils.createDensityQureg()(4, env)
    qureg2 = utils.createDensityQureg()(4, env)
    a = cheat.calcHilbertSchmidtDistance()(
        qureg1=qureg1,
        qureg2=qureg2,
    )
    assert a == 0.0


def test_calc_Expec_Pauli_Prod() -> None:
    """Test calculating the expectation value of a pauli product"""
    env = utils.createQuestEnv()()
    qubits = utils.createQureg()(4, env)
    workspace = utils.createQureg()(4, env)
    a = cheat.calcExpecPauliProd()(
        qureg=qubits,
        qubits=[0, 1, 2, 3],
        paulis=[0, 1, 3, 2],
        workspace=workspace,
    )
    assert a == 0.0


def test_seed() -> None:
    """Test seeding functions: seedQuEST, seedQuESTDefault"""
    cheat.seedQuEST()(seed_array=[0, 1, 2])
    cheat.seedQuESTDefault()()


def test_sync() -> None:
    """Test syncing functions: syncQuESTEnv, syncQuESTSuccess"""
    env = utils.createQuestEnv()()
    cheat.syncQuESTEnv()(env=env)
    success = cheat.syncQuESTSuccess()(success_code=0)
    assert success == 0


def test_basis_state_index_conversion() -> None:
    """Testing conversion basis state to index and index to basis state"""
    basis_state_1 = [0, 0, 1, 0, 1]
    index_1 = 20
    index_2 = 5

    index = cheat.basis_state_to_index(basis_state_1, endianness='little')
    npt.assert_array_equal(index, 20)
    index = cheat.basis_state_to_index(basis_state_1, endianness='big')
    npt.assert_array_equal(index, 5)

    basis_state = cheat.index_to_basis_state(index_1,
                                             num_qubits_represented=5,
                                             endianness='little')
    npt.assert_array_equal(basis_state, basis_state_1)
    basis_state = cheat.index_to_basis_state(index_2,
                                             num_qubits_represented=5,
                                             endianness='big')
    npt.assert_array_equal(basis_state, basis_state_1)


if __name__ == '__main__':
    pytest.main(sys.argv)
