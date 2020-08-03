"""Initialization objects in PyQuest-cffi"""
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
from typing import Union, List, Optional
import numpy as np
from pyquest_cffi.questlib import quest, _PYQUEST, tqureg, paulihamil
import warnings


class initZeroState(_PYQUEST):
    """Initialise zero state in quantum register

    Args:
        qureg: quantum register

    """

    def call_interactive(self, qureg: tqureg) -> None:
        """Interactive call of PyQuest-cffi

        Args:
            qureg: quantum register
        """
        quest.initZeroState(qureg)


class initPlusState(_PYQUEST):
    """Initialise plus state in quantum register

    Args:
        qureg: quantum register

    """

    def call_interactive(self, qureg: tqureg) -> None:
        """Interactive call of PyQuest-cffi

        Args:
            qureg: quantum register
        """
        quest.initPlusState(qureg)


class initClassicalState(_PYQUEST):
    """Initialization of classical state

    Initialise classic state, a classic integer in binary representation in the quantum register

    Args:
        qureg: The quantum register
        int: The integer that is initialised in binary representation in the quantum register

    """

    def call_interactive(self, qureg: tqureg, state: int) -> None:
        """Interactive call of PyQuest-cffi

        Args:
            qureg: quantum register
            state: The integer that is initialised in binary representation in the quantum register
        """
        quest.initClassicalState(qureg, state)


class initPureState(_PYQUEST):
    """Initialize a pure state

    Initialises a pure state in one wavefunction quantum register
    based on the pure state of another quantum register

    Args:
        qureg_a: Quantum register that is initialised
        qureg_b: Quantum register that contains the reference pure state

    """

    def call_interactive(self, qureg_a: tqureg, qureg_b: tqureg) -> None:
        """Interactive call of PyQuest-cffi

        Args:
            qureg_a: Quantum register that is initialised
            qureg_b: Quantum register that contains the reference pure state
        """
        quest.initPureState(qureg_a, qureg_b)


class initStateFromAmps(_PYQUEST):
    """Initialize a State from Amplitudes

    Initialise a wavefunction in a quantum register based on the real
    and imaginary parts of the statevector

    Args:
        qureg: the quantum register
        reals: The real parts of the statevector
        imags: The imaginary parts of the statevector

    """

    def call_interactive(self,
                         qureg: tqureg,
                         reals: Union[np.ndarray, List[float]],
                         imags: Union[np.ndarray, List[float]]
                         ) -> None:
        """Interactive call of PyQuest-cffi

        Args:
            qureg: the quantum register
            reals: The real parts of the statevector
            imags: The imaginary parts of the statevector
        """
        reals = list(reals)
        imags = list(imags)
        assert len(reals) == np.max(np.shape(reals))
        assert len(imags) == np.max(np.shape(imags))
        if qureg.isDensityMatrix:
            warnings.warn('qureg has to be a wavefunction qureg'
                          + ' but density matrix qureg was used', RuntimeWarning)
        else:
            quest.initStateFromAmps(qureg, reals, imags)


class initDebugState(_PYQUEST):
    """Debug class for state initialization"""

    def call_interactive(self, qureg: tqureg) -> None:
        """Interactive call of PyQuest-cffi

        Args:
            qureg: quantum register
        """
        quest.initDebugState(qureg)


class setAmps(_PYQUEST):
    """Set Amplitudes in statevector

    Set the values of elements of the statvector in a quantum register

    Args:
        qureg: The quantum register
        startind: The index of the first element of the statevector that is set
        reals: the new real values of the elements of the statevector
               between startind and startind+numamps
        imgas: the new imaginary values of the elements of the statevector
               between startind and startind+numamps
        numaps: the number of new values that are set in the statevector

    """

    def call_interactive(self,
                         qureg: tqureg,
                         startind: int,
                         reals: Union[np.ndarray, List[float]],
                         imags: Union[np.ndarray, List[float]],
                         numamps: int
                         ) -> None:
        """Interactive call of PyQuest-cffi

        Args:
            qureg: The quantum register
            startind: The index of the first element of the statevector that is set
            reals: the new real values of the elements of the statevector
                between startind and startind+numamps
            imags: the new imaginary values of the elements of the statevector
                between startind and startind+numamps
            numamps: the number of new values that are set in the statevector
        """
        reals = list(reals)
        imags = list(imags)
        assert len(reals) == np.max(np.shape(reals))
        assert len(imags) == np.max(np.shape(imags))
        assert len(reals) == numamps
        assert len(reals) == numamps
        if qureg.isDensityMatrix:
            warnings.warn('qureg has to be a wavefunction qureg'
                          + ' but density matrix qureg was used', RuntimeWarning)
        else:
            quest.setAmps(qureg, startind, reals, imags, numamps)

# cant find it in the API


class setDensityAmps(_PYQUEST):
    """Class setting the density matrix

    Set the values of elements of the vector representation
    of the density matrix in a quantum register

    Args:
        qureg: The quantum register of a density matrix
        reals: the new real values of the elements of the density matrix
               between startind and startind+numamps
        imgas: the new imaginary values of the elements of the density matrix
               between startind and startind+numamps

    """

    def call_interactive(self,
                         qureg: tqureg,
                         reals: Union[np.ndarray, List[float]],
                         imags: Union[np.ndarray, List[float]],
                         ) -> None:
        """Interactive call of PyQuest-cffi

        Args:
            qureg: The quantum register of a density matrix
            reals: the new real values of the elements of the density matrix
                between startind and startind+numamps
            imags: the new imaginary values of the elements of the density matrix
                between startind and startind+numamps
        """
        reals = list(reals)
        imags = list(imags)
        assert len(reals) == np.max(np.shape(reals))
        assert len(imags) == np.max(np.shape(imags))
        assert len(reals) == numamps
        assert len(reals) == numamps
        if not qureg.isDensityMatrix:
            warnings.warn('qureg has to be a density matrix qureg'
                          + ' but wavefunction qureg was used', RuntimeWarning)
        else:
            quest.setDensityAmps(qureg, reals, imags)


class setWeightedQureg(_PYQUEST):
    """Class setting a qureg as a weighted sum of two quregs

    Set the values of elements of the vector representation
    of the density matrix in a quantum register

    Args:
        fac1: prefactor of first qureg in sum
        qureg1: first qureg in sum
        fac2: prefactor of second qureg in sum
        qureg2: second qureg in sum
        facout: prefactor of output qureg
        quregout: output qureg

    """

    def call_interactive(self,
                         fac1: float,
                         qureg1: tqureg,
                         fac2: float,
                         qureg2: tqureg,
                         facout: float,
                         quregout: tqureg
                         ) -> None:
        """Interactive call of PyQuest-cffi

        Args:
            fac1: prefactor of first qureg in sum
            qureg1: first qureg in sum
            fac2: prefactor of second qureg in sum
            qureg2: second qureg in sum
            facout: prefactor of output qureg
            quregout: output qureg
        """
        quest.setWeightedQureg(fac1, qureg1, fac2, qureg2, facout, quregout)


class initBlankState(_PYQUEST):
    """Initialise classical zero state

    Args:
        qureg: qureg that is set to zero

    """

    def call_interactive(self,
                         qureg: tqureg,
                         ) -> None:
        """Interactive call of PyQuest-cffi

        Args:
            qureg: qureg that is set to zero
        """
        quest.initBlankState(qureg)


class initPauliHamil(_PYQUEST):
    """Initialise a PauliHamil instance

    Args:
        pauli_hamil: PauliHamil instance to initialise
        coeffs: array of coefficients
        codes: array of Pauli codes
    """

    def call_interactive(self,
                         pauli_hamil: paulihamil,
                         coeffs: List[float],
                         codes: List[int]) -> None:
        """Interactive call of PyQuest-cffi

        Args:
            pauli_hamil: PauliHamil instance to initialise
            coeffs: array of coefficients
            codes: array of Pauli codes
        """
        quest.initPauliHamil(pauli_hamil, coeffs, codes)
