<script lang="ts">
export const description = "Events management page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
} from "@/components/ui/dropdown-menu"

import {
  Plus,
  MoreHorizontal,
  Calendar,
  MapPin,
  Users,
} from "lucide-vue-next"

const userRole = "Admin"

// Dummy events data
const events = ref([
  {
    id: 1,
    title: "Orientation Day",
    date: "2024-01-20",
    organizer: "Admin Office",
    location: "School Gym",
    status: "Upcoming",
    type: "Academic",
    color: "bg-blue-500",
  },
  {
    id: 2,
    title: "Fire Safety Drill",
    date: "2024-01-15",
    organizer: "Safety Department",
    location: "Campus Grounds",
    status: "Completed",
    type: "General",
    color: "bg-green-500",
  },
  {
    id: 3,
    title: "Leadership Seminar",
    date: "2024-02-05",
    organizer: "Student Affairs",
    location: "AVR Room",
    status: "Upcoming",
    type: "Seminar",
    color: "bg-yellow-500",
  },
  {
    id: 4,
    title: "Foundation Day",
    date: "2023-12-10",
    organizer: "Admin Office",
    location: "Main Quadrangle",
    status: "Completed",
    type: "Celebration",
    color: "bg-red-500",
  },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all">
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Admin</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Events</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Top Bar -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Events</h2>
            <p class="text-sm text-muted-foreground">
              Manage school-wide events and important activities.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <Plus class="h-4 w-4" />
            Add Event
          </Button>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Events Overview</CardTitle>
            <CardDescription>
              View, edit, cancel, or track past and upcoming events.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex items-center justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search events..."
                class="max-w-xs"
              />
            </div>

            <!-- Table -->
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">Event</TableHead>
                  <TableHead>Date</TableHead>
                  <TableHead>Organizer</TableHead>
                  <TableHead>Location</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="ev in events"
                  :key="ev.id"
                  class="hover:bg-muted/50"
                >
                  <!-- Event Title -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <div class="h-3 w-3 rounded-full" :class="ev.color"></div>
                      <div>
                        <p class="font-medium">{{ ev.title }}</p>
                        <p class="text-xs text-muted-foreground">
                          {{ ev.type }}
                        </p>
                      </div>
                    </div>
                  </TableCell>

                  <!-- Date -->
                  <TableCell>
                    <div class="flex items-center gap-1">
                      <Calendar class="h-3 w-3 text-muted-foreground" />
                      <span>{{ ev.date }}</span>
                    </div>
                  </TableCell>

                  <!-- Organizer -->
                  <TableCell class="text-muted-foreground">
                    {{ ev.organizer }}
                  </TableCell>

                  <!-- Location -->
                  <TableCell>
                    <div class="flex items-center gap-1 text-muted-foreground">
                      <MapPin class="h-3 w-3" />
                      <span>{{ ev.location }}</span>
                    </div>
                  </TableCell>

                  <!-- Status -->
                  <TableCell>
                    <Badge
                      :variant="
                        ev.status === 'Upcoming'
                          ? 'default'
                          : ev.status === 'Completed'
                          ? 'secondary'
                          : 'destructive'
                      "
                    >
                      {{ ev.status }}
                    </Badge>
                  </TableCell>

                  <!-- Actions -->
                  <TableCell class="text-right">
                    <DropdownMenu>
                      <DropdownMenuTrigger as-child>
                        <Button variant="ghost" size="icon">
                          <MoreHorizontal class="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuSeparator />

                        <DropdownMenuItem>View Details</DropdownMenuItem>
                        <DropdownMenuItem>Edit Event</DropdownMenuItem>
                        <DropdownMenuItem>Mark as Completed</DropdownMenuItem>

                        <DropdownMenuSeparator />

                        <DropdownMenuItem class="text-red-600">
                          Delete Event
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </TableCell>

                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>

      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
