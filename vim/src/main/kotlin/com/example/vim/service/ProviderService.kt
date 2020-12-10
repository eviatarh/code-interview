package com.example.vim.service

import com.example.vim.dao.ProviderRepository
import com.example.vim.model.Appointment
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service

@Service
class ProviderService {

    @Autowired
    lateinit var providerRepo: ProviderRepository

    fun getProviders(specialty: String, date: Long, minScore: Float): List<String> {
        val providers = providerRepo.providers
        var matchingProviders: MutableList<String> = mutableListOf()
        for (provider in providers!!) {
            if (provider.score >= minScore && provider.specialties.contains(specialty.toLowerCase())) {
                for (availableDate in provider.availableDates) {
                    if (availableDate.from <= date && availableDate.to >= date) {
                        matchingProviders.add(provider.name)
                    }
                }
            }
        }

        return matchingProviders
    }

    fun schedule(appointment: Appointment): Boolean {
        val providers = providerRepo.providers
        for (provider in providers!!) {
            if (provider.name.equals(appointment.name, ignoreCase = true)) {
                for (availableDate in provider.availableDates) {
                    if (availableDate.from <= appointment.date && availableDate.to >= appointment.date) {
                        return true
                    }
                }
            }
        }
        return false
    }
}